import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

def fetch_url(text):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    return urls

def url_ranking(urls,counter=0,total=0):
    if(len(urls)==0):
        return [counter,total]
    for url in urls:
        if(bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")):
            rank=bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")['RANK']
            print("rank : "+str(rank))
            if(int(rank)<200000):
                counter=counter+1
            total=total+1
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
