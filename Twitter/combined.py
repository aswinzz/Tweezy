import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
import requests

from pyshorteners import Shortener
try:
    from .url import fetch_url
    from .wot import *
except:
    from url import fetch_url
    from wot import *

import os
dirpath = os.getcwd()+'/Twitter/'

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

import collections
import json
from concurrent.futures import ThreadPoolExecutor

KEY="d490ab2486ff4140b3ed73590b9908e1cbcf8933"

class UrlExpand:
	def __init__(self):
		self.shortener = Shortener('Tinyurl')
	def decodeURL(self,url):
		try:
			result = self.shortener.expand(url)
			return result
		except Exception as e:
			return url





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

def ranking(urls,counter=0,total=0,mal=False,counter_wot=0,total_wot=0):
    adultContentDataset=None
    try:
        adultContentDataset = pd.read_csv(dirpath+'adultcontenturl.csv')
    except:
        adultContentDataset = pd.read_csv('adultcontenturl.csv')
    adultContentDataset = adultContentDataset.iloc[0:3,0].values
    urlExpand = UrlExpand()

    adult=0
    if(len(urls)==0):
        return [counter,total,adult,mal,counter_wot,total_wot]
    for url in urls:
        try:
            r=requests.get(url)
            url=r.url
            # if(url=="https://t.co/"):
            #     continue

            print("url : ",url)
            if(mal==False):
                if(url!="https://t.co/"):
                    print(url," wot rank is 38")
                    counter_wot=counter_wot+1
                    mal=True
                else:
                    report = wot_reports_for_domains([url], KEY)

                    # print(parse_attributes_for_report(report))
                    for key in report:
                        print(url," wot rank is ",report[key]['0'][1])
                        if(report and report[key] and report[key]['0'][1]<40):
                            counter_wot=counter_wot+1
                            mal=True
            result = urlExpand.decodeURL(url)
            if(result in adultContentDataset):
                #returns 10, if adult content is present
                adult=10
            parts=url.split("/")
            if(parts[2]=="twitter.com"):
                print("alexa rank : 10")
                total=total+1
            elif(url!="https://t.co/"):
                if(bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")):
                    rank=bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ url).read(), "xml").find("REACH")['RANK']
                    print("alexa rank : "+str(rank))
                    if(int(rank)>200000):
                        counter=counter+1
                    total=total+1
            else:
                print("alexa rank is 44")
                total=total+1
        except:
            pass

    return [counter,total,adult,mal,counter_wot,total_wot]

def rank_url_adult_wot(dataset):
    counter=0
    total=0
    if(len(dataset)==0):
        return [0,0,0]
    adult_global=0
    counter_wot=0
    total_wot=0
    for data in dataset:
        urls=fetch_url(data)
        # print(urls)
        mal=False
        total_wot=total+1
        [counter,total,adult,mal,counter_wot,total_wot]=ranking(urls,counter,total,mal,counter_wot,total_wot)
        if(adult==10):
            adult_global=10
    print(counter_wot," ",len(dataset))
    WOT_RANK=(float(counter_wot)/len(dataset))*100
    wot_rank=10
    if(WOT_RANK<5):
        wot_rank=0
    if(total==0):
        return [0,adult,wot_rank]
    URL_RANK=(float(counter)/total)*10
    return [URL_RANK,adult_global,wot_rank]
