import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from url import rank_url
from similarity import rank_similarity

dataset = pd.read_csv('text_emotion.csv')
dataset = dataset.iloc[0:20,3].values

print(rank_url(dataset))
print(rank_similarity(dataset))
