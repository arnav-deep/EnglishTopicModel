import logging
import gensim
from gensim.test.utils import datapath
from gensim.models.ldamodel import LdaModel


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('WikiCorpus/wiki_wordids.txt')
mm = gensim.corpora.MmCorpus('WikiCorpus/wiki_tfidf.mm')
print(mm)

lda = LdaModel(corpus=mm, id2word=id2word, num_topics=130, update_every=1, passes=1)

model_location = datapath("D:/HazMat/Projects/ML/Models/model_130")
lda.save(model_location)
