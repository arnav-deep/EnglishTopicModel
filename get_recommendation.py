import pandas as pd
from gensim.test.utils import datapath
from gensim.models.ldamodel import LdaModel
from gensim.matutils import jensen_shannon

model_location = datapath("D:/HazMat/Projects/ML/Models/model_130")
model = LdaModel.load(model_location)

lda_bow = []
with open('movie_lda_bow.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        idprob = []
        num_line = line.replace("[", "").replace("(", "").replace(",", "").replace(")", "").replace("]", "").split(" ")
        i = 0
        if len(num_line) > 2:
            for num in num_line:
                # print(num)
                if i % 2 == 0:
                    word = int(num)
                else:
                    prob = float(num)
                if i % 2 == 1:
                    idprob.append([word, prob])
                i += 1
            lda_bow.append(idprob)

print(len(lda_bow))
# df_input = pd.read_csv('Datasets/wiki_movie_plots_deduped.csv')
#
# titles = df_input.Title
# plots_raw = df_input.Plot
# links = df_input.Wikilink
#
# print(titles[5], titles[4], jensen_shannon(lda_bow[4], lda_bow[5], 130))
# print(titles[5], titles[32], jensen_shannon(lda_bow[5], lda_bow[32], 130))
# print(titles[35], titles[32], jensen_shannon(lda_bow[35], lda_bow[32], 130))
# print(titles[80], titles[4], jensen_shannon(lda_bow[80], lda_bow[4], 130))
