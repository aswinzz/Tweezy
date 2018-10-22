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

from url import rank_url,fetch_url
from similarity import rank_similarity
from wot import *
from checkContent import checkAdultContent
from checkTime import rank_time

KEY="d490ab2486ff4140b3ed73590b9908e1cbcf8933"

consumer_key = "eoWSW9nGuDnuetWn5DuRbV1Xp"
consumer_secret = "JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj"
access_key = "1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS"
access_secret = "poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk"

#dataset = pd.read_csv('text_emotion.csv')
#datasetWithTime = pd.read_csv('tweet_date.csv')

#dataset = dataset.iloc[0:500,3].values
#datasetWithTime = datasetWithTime.iloc[0:100,2].values

print("***********************************")
#print(dataset)
print("***********************************")

# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
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

if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    [tweet_textList,tweet_timeList] = get_tweets("aswanth9495")
    
    print("URL RANKING : ",rank_url(tweet_textList))
    print("SIMILARITY RANKING : ",rank_similarity(tweet_textList))
    print("WOT RANKING : ",rank_wot(tweet_textList))
    print("ADULT CONTENT : ",checkAdultContent(tweet_textList))
    print("TIME RANKING : ",rank_time(tweet_timeList))
