import numpy as np
import pandas as pd

from gensim.corpora import Dictionary
from gensim.test.utils import datapath
from gensim.models.ldamodel import LdaModel
from gensim.models import TfidfModel
from gensim.matutils import jensen_shannon
from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string, strip_non_alphanum, strip_numeric, \
    strip_short

np.seterr(divide='ignore', invalid='ignore')

df_input = pd.read_csv('Datasets/wiki_movie_plots_deduped.csv')

titles = df_input.Title
plots_raw = df_input.Plot
links = df_input.Wikilink

plots = []
for plot in plots_raw:
    temp = plot.lower()
    temp = strip_non_alphanum(temp)
    temp = strip_numeric(temp)
    temp = remove_stopwords(temp)
    temp = strip_short(temp)
    temp = preprocess_string(temp)
    plots.append(temp)

model_location = datapath("D:/HazMat/Projects/ML/Models/model_130")
model = LdaModel.load(model_location)

bow_plot = []
lda_bow = []
for plot in plots:
    bow_plot.append(model.id2word.doc2bow(plot))

for bow in bow_plot:
    lda_bow.append(model[bow])

df_res = pd.DataFrame({"title": [],
                       "rec": []})

df_title = pd.DataFrame({"title": [],
                         "dist": []})

for i in range(len(titles)):
    df_title.empty
    df_curr = pd.DataFrame({"title": [titles[i]]})
    for j in range(len(lda_bow)):
        if j != i:
            dst = jensen_shannon(lda_bow[i], lda_bow[j], 130)
            df_individual = pd.DataFrame({"title": [titles[j]],
                                          "dist": [dst]})
            df_title = df_title.append(df_individual, ignore_index=True)

    df_title = df_title.sort_values(by=['dist'])
    df_rec = pd.DataFrame({"rec": [df_title['title'][0:50]]})
    df_ind_res = pd.merge(df_curr, df_rec, left_index=True, right_index=True, how='inner')
    df_res = df_res.append(df_ind_res, ignore_index=True)
