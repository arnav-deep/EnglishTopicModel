# Recommendation System using LDA
A Topic Modelling model is created using LDA from gensim library. LDA can be understood from this [youtube video](https://www.youtube.com/watch?v=3mHy4OSyRf0).

Clone this repository on your laptop or download files by clicking [here](https://github.com/arnav-deep/EnglishTopicModel/archive/master.zip).

# Making Basic Enlgish Model
A model for Topic Modelling using LDA is made by using the [gensim](https://pypi.org/project/gensim/) library.

# What it can be used for?
This Topic Modelling Model can be used for any English Database. To see an example of how it can be used for Movie Recommendation, check out this [repository](https://github.com/arnav-deep/MovieRecommendation).

# Dataset
For the model, Wikipedia dump has been used as the Dataset, which has over 4 million articles in English. The dataset can be found [here](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2). The dataset size is 16.2 GB.

# Requirements
Written in [requirements.txt](https://github.com/arnav-deep/EnglishTopicModel/blob/master/requirements.txt). Using a virtual environment is recommended.
```python
pip install -r requirements.txt
```

# Preprocessing Dataset and making gensim corpus
The code for tpreprocessing dataset is written in [create_wiki_corpus.py](https://github.com/arnav-deep/EnglishTopicModel/blob/master/create_wiki_corpus.py).<br>
Note: This process will take around 10 hours to complete. Output file is a gensim corpus of size 34.6 GB, so it's not uploaded.

# Training the Model
The code to train the model is written in the script [train_lda_model.py](https://github.com/arnav-deep/EnglishTopicModel/blob/master/train_lda_model.py).<br>
The model has been trained via unsupervised learning on the complete dataset of all Wikipedia English articles. The number of topics trained on the model is 130.<br>
Note: This process will take around 6 hours to complete. The model files have already been saved here in the [Models](https://github.com/arnav-deep/EnglishTopicModel/tree/master/Models) folder.

# Checking the model
The code for checking the topics inside the model can be found in [show_model_topics.py](https://github.com/arnav-deep/EnglishTopicModel/blob/master/show_model_topics.py).<br>
Run the code to see the topics. The topics have a number id. It can be seen that the words in the topics have similaritites among them.<br>
Model can be improved by tweaking the number of topics. This strictly depends on usage.

```python
python load_model.py
```
This will return list of topics the model has made.

## License
GNU GENERAL PUBLIC LICENSE Version 2

Arnav Deep © June 2020. All rights reserved.
