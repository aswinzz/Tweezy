import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def cosine_sim(str1,str2):

    vector1 = text_to_vector(str1)
    vector2 = text_to_vector(str2)

    cosine = get_cosine(vector1, vector2)

    if(cosine>0.75):
        return 1
    return 0


def rank_similarity(dataset):
    counter=0
    total=0
    for i in range(2,len(dataset)-3):
        total=total+1
        hitinCluster = 0
        for j in range(i-3,i+4):
            if(j>0 and j<len(dataset)):
                for k in range(j+1,i+4):
                    if(j!=k and k>0 and k<len(dataset)):
                        if(cosine_sim(dataset[j],dataset[k])):
                            counter = counter+1
                            hitinCluster = 1
                            break
            if(hitinCluster==1):
                break

    if(total==0):
        return 0
    print(counter," of ",total," clusters are similar")
    similarity_rank=(float(counter)/total)*10
    return similarity_rank

# def rank_similarity(dataset):
#     counter=0
#     total=0
#     for i in range(0,len(dataset)):
#         total=total+1
#         for j in range(i-3,i+3):
#             if(j>0 and j<len(dataset)):
#                 for k in range(i-3,i+3):
#                     if(j!=k and k>0 and k<len(dataset)):
#                         counter=counter+cosine_sim(dataset[j],dataset[k])
#                         if(cosine_sim(dataset[j],dataset[k])):
#                             print("yes : "+str(j)+" : "+str(k))
#     print(counter)
#     print(total)
#     similarity_rank=(float(counter)/total)*10
#     return similarity_rank
