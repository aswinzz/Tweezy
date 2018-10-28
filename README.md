# TWEEZY
<img src="main/static/main/icon-left-font.png" width = "700" height= "200">
<br>

Classify Twitter users based on different parameters

## Basic Idea
A twitter user is classified into Anomalous, Non Anomalous and Intermediate using 5 parameters and each of these parameter will be given a rank:
- Time Difference (denoted by a)
- Similarity of Tweets (b)
- URL Ranking (c)
- Malware URL (d)
- Adult Content (e)


each of these parameter will be assigned a value from 1-10 for each user and these parameters have a weight which together will decide whether a user is anomalous or not

Weights of each parameter are :
- Time Difference: 0.15
- Similarity of Tweets: 0.25
- URL Ranking: 0.30
- Malware URL: 0.30
- Adult Content: 1

### An FAL value is assigned combining all these parameters which is given by
![](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/8123903/8203898/8204141/8204141-alg-1-source-small.gif)

### Depending upon the FAL value , a user can be classified into Anomalous, Non Anomalous and Intermediate
![](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/8123903/8203898/8204141/8204141-table-1-source-small.gif)


## Classification
- This algorithm is applied on a dataset of twitter users from which a dataset of a,b,c,d,e and FAL values are obtained.
- Onto this dataset different classification methods are applied.

## Classification Methods Used
- K-nearest neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes classifiers
- Random Forest
- Decision Tree

## Structure
* Files related to algorithm used is present in Twitter folder
* Main.py is the root file to be run from which other functions are called
* dataset_generator.py generates dummy data of values a,b,c,d,e,FAL,type into dataset_gen.csv
* Classifier.py takes in the data present in the dataset_gen.csv and classify the users based on different Classification Algorithm
* wot.py is used to calculate Web Of Trust Rank
* similarity.py is used to calculate similarity of tweets
* url.py is used to calculate Alexa rank of url's present in the tweets
* checkTime.py is used to calculate time difference of tweets
* checkContent.py is used to check for adult contents in tweets

## How to run ?
To check whether a particular user is anomalous :-
- clone this repo
- run the following commands in the terminal from the cloned folder
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- open `localhost:8000/main` in your browser

To do the classification follow these steps :-
- open Twitter folder in terminal
- store the dataset of usernames which needs to be classified in  `dataset_gen.csv`
- run `python main.py`
- output based on 5 classification algorithm will be displayed as the output

# Screenshots

![1](screenshots/3.png)
![2](screenshots/4.png)
![3](screenshots/5.png)
![4](screenshots/6.png)
