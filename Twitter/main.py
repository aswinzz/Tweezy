import tweepy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from .url import rank_url,fetch_url
    from .similarity import rank_similarity
    from .wot import *
    from .checkContent import checkAdultContent
    from .checkTime import rank_time
    from .Classifier import *
except:
    from url import rank_url,fetch_url
    from similarity import rank_similarity
    from wot import *
    from checkContent import checkAdultContent
    from checkTime import rank_time
    from Classifier import *
import csv


KEY="d490ab2486ff4140b3ed73590b9908e1cbcf8933"

consumer_key = "eoWSW9nGuDnuetWn5DuRbV1Xp"
consumer_secret = "JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj"
access_key = "1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS"
access_secret = "poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk"

#dataset = pd.read_csv('text_emotion.csv')
#datasetWithTime = pd.read_csv('tweet_date.csv')

#dataset = dataset.iloc[0:500,3].values
#datasetWithTime = datasetWithTime.iloc[0:100,2].values

# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username,count=number_of_tweets)
        tweet_textList=[]
        tweet_timeList=[]

        tweets_text = [tweet.text for tweet in tweets]
        tweets_time = [tweet.created_at for tweet in tweets]

        for i in tweets_text:
            tweet_textList.append(i)
            print(i)
        print("\n")
        for i in tweets_time:
            tweet_timeList.append(i)
            print(i)
        return tweet_textList,tweet_timeList
    except:
        print("Error")
        return [],[]

def singleuser(username):
    [tweet_textList,tweet_timeList] = get_tweets(username)
    if(len(tweet_textList)!=0 and len(tweet_timeList)!=0):
        a=rank_time(tweet_timeList)
        b=rank_similarity(tweet_textList)
        c=rank_url(tweet_textList)
        d=rank_wot(tweet_textList)
        e=checkAdultContent(tweet_textList)

        print("URL RANKING : ",c)
        print("SIMILARITY RANKING : ",b)
        print("WOT RANKING : ",d)
        print("ADULT CONTENT : ",e)
        print("TIME RANKING : ",a)

        FAL=0
        if(e!=10):
            FAL=a*0.15+b*0.25+c*0.3+d*0.3
        type=0
        if(FAL>=4 and FAL<=5):
            type=1
        if(FAL>5 and FAL<=10):
            type=2

        return [a,b,c,d,e,FAL,type]
    else:
        return ["empty"]

def analyser():
    dataset = pd.read_csv('Followers.csv')
    usernames = dataset.iloc[1:, [0]].values
    lines=[]
    for username in usernames:
        print(username[0])
        [tweet_textList,tweet_timeList] = get_tweets(username[0])
        if(len(tweet_textList)!=0 and len(tweet_timeList)!=0):
            a=rank_time(tweet_timeList)
            b=rank_similarity(tweet_textList)
            c=rank_url(tweet_textList)
            d=rank_wot(tweet_textList)
            e=checkAdultContent(tweet_textList)

            print("URL RANKING : ",c)
            print("SIMILARITY RANKING : ",b)
            print("WOT RANKING : ",d)
            print("ADULT CONTENT : ",e)
            print("TIME RANKING : ",a)

            FAL=0
            if(e!=10):
                FAL=a*0.15+b*0.25+c*0.3+d*0.3
            type=0
            if(FAL>=4 and FAL<=5):
                type=1
            if(FAL>5 and FAL<=10):
                type=2

            lines.append([a,b,c,d,e,FAL,type])
        else:
            print("Empty")

    with open('dataset_gen.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()
    dataset = pd.read_csv('dataset_gen.csv')
    cm_knn=KNN(dataset)
    cm_nb=NaiveBayesClassifier(dataset)
    cm_dt=DecisionTree(dataset)
    cm_rf=RandomForest(dataset)
    cm_svm=SVM(dataset)
    print("KNN Classification")
    print("==================")
    print(cm_knn)
    print()
    print("Naive Bayes Classification")
    print("==========================")
    print(cm_nb)
    print()
    print("Decistion Tree Classification")
    print("=============================")
    print(cm_dt)
    print()
    print("Random Forest Classification")
    print("============================")
    print(cm_rf)
    print()
    print("SVM Classification")
    print("==================")
    print(cm_svm)

    return [cm_knn,cm_nb,cm_dt,cm_rf,cm_svm]

if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    temp=analyser()
