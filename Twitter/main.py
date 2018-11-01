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
import datetime

try:
    from url import rank_url,fetch_url
    from similarity import rank_similarity
    from wot import *
    from checkContent import checkAdultContent
    from checkTime import rank_time
    from Classifier import *
    from combined import rank_url_adult_wot
except:
    from .url import rank_url,fetch_url
    from .similarity import rank_similarity
    from .wot import *
    from .checkContent import checkAdultContent
    from .checkTime import rank_time
    from .Classifier import *
    from .combined import rank_url_adult_wot

import csv
import math

KEY="d490ab2486ff4140b3ed73590b9908e1cbcf8933"

consumer_key = "eoWSW9nGuDnuetWn5DuRbV1Xp"
consumer_secret = "JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj"
access_key = "1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS"
access_secret = "poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk"

#dataset = pd.read_csv('text_emotion.csv')
#datasetWithTime = pd.read_csv('tweet_date.csv')

#dataset = dataset.iloc[0:500,3].values
#datasetWithTime = datasetWithTime.iloc[0:100,2].values



def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper

def findAccuracy(cm,dimension):
    tot=0
    dia=0
    for i in range(0,dimension[0]):
        for j in range(0,dimension[0]):
            tot += cm[i][j]
            if(i==j):
                dia += cm[i][j]
    print("Accuracy : "+str((dia/tot)*100))

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
    if(tweet_timeList):
        if(tweet_timeList[0] == -1):
            return [0,0,0,0,0,0,-1]
    if(len(tweet_textList)!=0 and len(tweet_timeList)!=0):
        a=0
        b=0
        c=0
        d=0
        e=0

        a=rank_time(tweet_timeList)
        b=rank_similarity(tweet_textList)
        # c=rank_url(tweet_textList)
        # d=rank_wot(tweet_textList)
        # e=checkAdultContent(tweet_textList)
        [c,e,d]=rank_url_adult_wot(tweet_textList)
        a=truncate(a,2)
        b=truncate(b,2)
        c=truncate(c,2)
        d=truncate(d,2)
        e=truncate(e,2)
        print("Output")
        print("------")
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
        FAL=truncate(FAL,2)
        print("FAL : ",FAL)
        if(type==0):
            print("The entered user is Non Anomalous")
        elif(type==1):
            print("The entered user is suspected")
        else:
            print("The entered user is Anomalous")
        return [a,b,c,d,e,FAL,type]
    else:
        return ["empty"]

def analyser(need_fetch,size=0):
    start=datetime.datetime.now()
    dataset = pd.read_csv('Followers.csv')
    usernames = dataset.iloc[1:, [0]].values
    lines=[]
    if(need_fetch):
        for l in range(0,size):
            username=usernames[l]
        # for username in usernames:
            print(username[0])
            [tweet_textList,tweet_timeList] = get_tweets(username[0])
            if(len(tweet_textList)!=0 and len(tweet_timeList)!=0):
                a=rank_time(tweet_timeList)
                b=rank_similarity(tweet_textList)
                # c=rank_url(tweet_textList)
                # d=rank_wot(tweet_textList)
                # e=checkAdultContent(tweet_textList)
                [c,e,d]=rank_url_adult_wot(tweet_textList)

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
    findAccuracy(cm_knn,cm_knn.shape)
    print()
    print("Naive Bayes Classification")
    print("==========================")
    print(cm_nb)
    findAccuracy(cm_nb,cm_nb.shape)
    print()
    print("Decistion Tree Classification")
    print("=============================")
    print(cm_dt)
    findAccuracy(cm_dt,cm_dt.shape)
    print()
    print("Random Forest Classification")
    print("============================")
    print(cm_rf)
    findAccuracy(cm_knn,cm_knn.shape)
    print()
    print("SVM Classification")
    print("==================")
    print(cm_svm)
    findAccuracy(cm_svm,cm_svm.shape)
    print()
    print("Completed")
    end=datetime.datetime.now()
    print("end time ",end)
    print(end-start)
    return [cm_knn,cm_nb,cm_dt,cm_rf,cm_svm]

if __name__ == '__main__':
    type="3"
    while(True):
        print("Choose which type to use :")
        print("1) Single User")
        print("2) Multiple Users (Classification)")
        type=input()
        if(type=="1"):
            break
        elif(type=="2"):
            break
        else:
            print("Invalid Input (Enter 1 or 2)")
    if(type=="1"):
        print("Enter the username to be analysed")
        username=input()
        temp=singleuser(username)
    elif(type=="2"):
        x="A"
        fetch_val=False
        size=0
        while(True):
            print("Do you need to create the dataset of a,b,c,d,e values (Y/N) or just use the prebuilt dataset")
            x=input()
            if(x=="Y"):
                print("How much usernames to be used ? (0-500)")
                size=int(input())
                fetch_val=True
                break
            elif(x=="N"):
                break
            else:
                print("Invalid Input , Enter Y or N")
        temp=analyser(fetch_val,size)
