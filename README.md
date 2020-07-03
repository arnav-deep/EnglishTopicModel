ML Project by Arnav Deep (2017316), Kaushal Sharma (2017324) and Shivam Dubey (2017349)

For comfortable viewing, please read on my GitHub repository.<br>
Open from this link: https://github.com/arnav-deep/RecommendationLDA

Contact for queries: arnavd4@gmail.com - Arnav Deep<br>

# Recommendation System using LDA
A Topic Modelling model is created using LDA from gensim library. LDA can be understood from this [youtube video](https://www.youtube.com/watch?v=3mHy4OSyRf0).

Clone this repository on your laptop or download files by clicking [here](https://github.com/arnav-deep/RecommendationLDA/archive/master.zip).

## Making Basic Enlgish Model
A model for Topic Modelling using LDA is made by using the [gensim](https://pypi.org/project/gensim/) library.

### Dataset
For the model, Wikipedia dump has been used as the Dataset, which has over 4 million articles in English. The dataset can be found [here](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2). The dataset size is 16.2 GB.

### Requirements
Written in [requirements.txt](https://github.com/arnav-deep/RecommendationLDA/blob/master/requirements.txt). Using a virtual environment is recommended.
```python
pip install -r requirements.txt
```

### Preprocessing Dataset and making gensim corpus
The code for tpreprocessing dataset is written in [create_wiki_corpus.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/create_wiki_corpus.py).<br>
Note: This process will take around 10 hours to complete. Output file is a gensim corpus of size 34.6 GB, so it's not uploaded.

### Training the Model
The code to train the model is written in the script [train_lda_model.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/train_lda_model.py).<br>
The model has been trained via unsupervised learning on the complete dataset of all Wikipedia English articles. The number of topics trained on the model is 130.<br>
Note: This process will take around 6 hours to complete. The model files have already been saved here in the [Models](https://github.com/arnav-deep/RecommendationLDA/tree/master/Models) folder.

### Checking the model
The code for checking the topics inside the model can be found in [show_model_topics.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/show_model_topics.py).<br>
Run the code to see the topics. The topics have a number id. It can be seen that the words in the topics have similaritites among them.<br>
Model can be improved by tweaking the number of topics. This strictly depends on usage.

```python
python load_model.py
```

## Movie Recommendation
All files related to Movie Recommendation can be found in the [movie_rec](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec) folder.

### Dataset
The dataset used is taken from Kaggle and can be found [here](https://www.kaggle.com/jrobischon/wikipedia-movie-plots).

### Preprocess dataset
The dataset is required to be preprocessed. This is done through the python script [movie_lda_bow.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/movie_lda_bow.py). This outputs a gensim lda2bow which is a txt file storing values of the probability distribution value of its topic which has been assigned to every word in the dataset.<br>
Probabilty distribution value between two plots can be calculated using Jensen-Shannon Divergence.<br>
Output of this script, the lda2bow data, is stored in [model_ldabow.txt](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/movie_ldabow.txt)

### Method to get recommendations
I have created two different methods to get recommendations. 

Note: The CSV method is computationaly very heavy, so that's not recommended unless being used for production. It takes around 27 hours for 1000 movies and our movie dataset contains over 35,000 movies.

#### A. Directly from terminal
Video showing how this method works can be found [here](https://drive.google.com/open?id=1zKI9-WiZsM4FT4043dBx4PGDZ4NXI4As).

The python script, [get_rec.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/get_rec.py) has been written to get recommendations. It can be run and tested by giving movie tiltes present in the dataset as input.<br>
Note: You can get the movies present in the dataset from [movie_titles.txt](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/movie_titles.txt) or you can run simply run [get_rec.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/get_rec.py) and the terminal will help you get the movie titles.
```python
python get_rec.py
```
Instructions to use the script can be found in the terminal when script is run.

#### B. Save it to CSV
Model takes words as input. Each word of an input data must be fed. The code can be found in [movie_rec_csv.py](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/movie_rec_csv.py). This outputs a CSV with movie title and its top 50 recommendations in order.<br>
Note: Dataset must be downloaded before running this script. The output CSV after running this script for i=100 movies is already stored in [movie_recommendation.csv](https://github.com/arnav-deep/RecommendationLDA/blob/master/movie_rec/movie_recommendation.csv).

## What more can be done
1. Any other Dataset can be taken, just like the movie dataset is taken and used to get recommendations.<br>
The procedure will be very simple and the steps to be followed will be the same as that of this movie recommendation.<br>

2. A movie plot in the form of a string can be input in get_rec.py and the model can be run on it to get recommendations from the data.<br>

3. A website can be based using this model, but using the CSV method will be better and give fast results.
