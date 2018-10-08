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

def url_ranking(urls):
    counter=0
    total=0
    for url in urls:
        rank=bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ urls[0]).read(), "xml").find("REACH")['RANK']
        print(rank)
        if(int(rank)<200000):
            counter=counter+1
        total=total+1
    URL_RANK=(counter/total)*10
    return URL_RANK
