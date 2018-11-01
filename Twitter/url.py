import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
import requests

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

def fetch_url(text):
    urls_check1 = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
    urls_check2 = re.findall(regex, text)

    urls=[]

    #combining all in urls
    for item in urls_check1:
        if item not in urls:
            urls.append(item)
    for item in urls_check2:
        if item not in urls:
            urls.append(item)

    # print(urls)
    return urls

def url_ranking(urls,counter=0,total=0):
    if(len(urls)==0):
        return [counter,total]
    for url in urls:
        try:
            r=requests.get(url)
            url=r.url
            parts=url.split("/")
            if(parts[2]=="twitter.com"):
                total=total+1
            elif(url!="https://t.co/"):
                print(url)
                if(bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")):
                    rank=bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")['RANK']
                    print("rank : "+str(rank))
                    if(int(rank)>150000):
                        counter=counter+1
                    total=total+1
            else:
                total=total+1
        except:
            print("cannot check url")

    return [counter,total]

def rank_url(dataset):
    counter=0
    total=0
    if(len(dataset)==0):
        return 0
    for data in dataset:
        urls=fetch_url(data)
        # print(urls)
        [counter,total]=url_ranking(urls,counter,total)
    if(total==0):
        return 0
    URL_RANK=(float(counter)/total)*10
    return URL_RANK
