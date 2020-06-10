from gensim.test.utils import datapath
from gensim.models.ldamodel import LdaModel

model_location = datapath('D:/HazMat/Projects/ML/Models/model_130')
model = LdaModel.load(model_location)

print(model.print_topics(10))
