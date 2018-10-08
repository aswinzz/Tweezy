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
KEY="d490ab2486ff4140b3ed73590b9908e1cbcf8933"

dataset = pd.read_csv('text_emotion.csv')
dataset = dataset.iloc[0:20,3].values

print("URL RANKING : ",rank_url(dataset))
print("SIMILARITY RANKING : ",rank_similarity(dataset))
print("WOT RANKING : ",rank_wot(dataset))
