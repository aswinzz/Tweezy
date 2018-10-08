import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from url import url_ranking,fetch_url
from similarity import cosine_sim

dataset = pd.read_csv('text_emotion.csv')
str1="AI is our friend and it has been friendly"
str2="AI and humans have always been friendly"
print(cosine_sim(str1,str2))

text="asdkad;lad https://geeksforgeeks.org"
urls=fetch_url(text)
print(urls)
print(url_ranking(urls))
