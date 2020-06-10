"""
USAGE: %(program)s WIKI_XML_DUMP OUTPUT_PREFIX [VOCABULARY_SIZE]

Example:
  python -m gensim.scripts.make_wikicorpus ~/gensim/results/enwiki-latest-pages-articles.xml.bz2 ~/gensim/results/wiki
"""

import logging
import os.path
import sys

from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.models import TfidfModel

DEFAULT_DICT_SIZE = 100000

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s", ' '.join(sys.argv))

    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp = sys.argv[1:3]

    if not os.path.isdir(os.path.dirname(outp)):
        raise SystemExit("Error: The output directory must be different than input. Create a new folder and try again")

    if len(sys.argv) > 3:
        keep_words = int(sys.argv[3])
    else:
        keep_words = DEFAULT_DICT_SIZE
    online = 'online' in program
    lemmatize = 'lemma' in program
    debug = 'nodebug' not in program

    if online:
        dictionary = HashDictionary(id_range=keep_words, debug=debug)
        dictionary.allow_update = True
        wiki = WikiCorpus(inp, lemmatize=lemmatize, dictionary=dictionary)
        MmCorpus.serialize(outp + '_bow.mm', wiki, progress_cnt=10000, metadata=True)
        dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
        dictionary.save_as_text(outp + '_wordids.txt.bz2')
        wiki.save(outp + '_corpus.pkl.bz2')
        dictionary.allow_update = False
    else:
        wiki = WikiCorpus(inp, lemmatize=lemmatize)
        wiki.dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
        MmCorpus.serialize(outp + '_bow.mm', wiki, progress_cnt=10000, metadata=True)
        wiki.dictionary.save_as_text(outp + '_wordids.txt.bz2')
        dictionary = Dictionary.load_from_text(outp + '_wordids.txt.bz2')
    del wiki

    mm = MmCorpus(outp + '_bow.mm')

    tfidf = TfidfModel(mm, id2word=dictionary, normalize=True)
    tfidf.save(outp + '.tfidf_model')

    MmCorpus.serialize(outp + '_tfidf.mm', tfidf[mm], progress_cnt=10000)

    logger.info("finished running %s", program)
