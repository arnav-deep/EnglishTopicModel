ML Project by Arnav Deep (2017316), Kaushal Sharma (2017324), Shivam Dubey (2017349)

For comfortable viewing, please read on my GitHub repository.<br>
Open from this link: https://github.com/arnav-deep/RecommendationLDA<br>
Contact for queries: +91-9408597449, 2017316@iiitdmj.ac.in - Arnav Deep<br>

# Recommendation System using LDA
A Topic Modelling model is created using LDA from gensim library.

### Dataset
For the model, Wikipedia dump has been used as the Dataset, which has over 4 million articles in English. The dataset can be found [here](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2). The data is of 15.9 GB.

### Requirements
Written in [requirements.txt](https://github.com/arnav-deep/RecommendationLDA/blob/master/requirements.txt).

```python
pip install -r requirements.txt
```
### Preprocessing Dataset and making gensim corpus
The code for the same is written in [create_wiki_corpus.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/create_wiki_corpus.py).<br>
Note: This process will take around 10 hours to complete. Output file is of size 34.6 GB, so it's not uploaded.

### Training the Model
The code to train the model is written in the script [train_lda_model.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/train_lda_model.py).<br>
The model has been trained via unsupervised learning on the complete articles of all Wikipedia English. The number of topics trained on model is 130.<br>
Note: This process will take 6 hours to complete. The model files have already been saved in the 'Models' folder.

### Checking the model
The code for checking what the topics inside the model are can be found in [load_model.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/load_model.py).<br>
Run the code to see the topics. The topics have a number id. It can be seen that the words in the topics have similaritites among them.<br>
Model can be improved by tweaking the number of topics as per requirement.

```python
python load_model.py
```

## Movie Recommendation

### Dataset
The dataset used is taken from Kaggle and can be found [here](https://www.kaggle.com/jrobischon/wikipedia-movie-plots).

### Creating recommendations
Model takes words as input. Each word of an input data must be fed. The code can be found in [movie_rec.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec.py). This outputs a CSV with movie title and its top 50 recommendations in order.<br>
Note: Takes around 30 minutes to run. Dataset must be downloaded before running this script, although running it is not necessary as the output [movie_recommendations.csv](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_recommendations.csv) is already uploaded.

### Runnning recommendations
The python script, [get_rec.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/get_rec.py) has been written to get recommendations from this csv. It can be run and tested by giving movie tiltes present in the dataset as input.<br>
Note: You can get the movies present in the dataset from [movie_titles.txt](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_titles.txt) or you can run simply run [get_rec.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/get_rec.py) and the terminal will help you get the movie titles.
```python
python get_rec.py
```

## What more can be done
1. Any other Dataset can be taken, just like the movie dataset is taken and used to get recommendations.<br>
The procedure will be very simple and the steps to be followed will be the same as that of this movie recommendation.<br>

2. A movie plot in the form of a string can be input in get_rec.py and the model can be run on it to get recommendations from the data.
