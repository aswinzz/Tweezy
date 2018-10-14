import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from pyshorteners import Shortener
from url import fetch_url

def findTimeDiff(dataset,pos1,pos2):
	t1 = dataset[pos1]
	t2 = dataset[pos2]
	t1 = t1.split(" ")
	t2 = t2.split(" ")
	if((t1[5]==t2[5]) and (t1[1]==t2[1]) and (t1[2]==t2[2])):
		t1 = t1[3].split(":")
		t2 = t2[3].split(":")
		if((int(t1[0])*3600+int(t1[1])*60+int(t1[2]))-(int(t1[0])*3600+int(t1[1])*60+int(t1[2])) < 120):
			return 1
		else:
			return 0

def rank_time(dataset):
	cluster=0
	hits=0
	if(len(dataset) < 7):	#cannot predict
		return 0
	#7 tweets is taken as a cluster
	for i in range(0,len(dataset)-6):
		for j in range(0,3):
			if(findTimeDiff(dataset,i+j,i+j+4)):	#check time taken for 5 tweets,ie time difference of ith and i+4th tweet
				hits = hits+1
				break
	cluster=len(dataset)-6

	rank = (float(hits)/cluster)*10
	return rank




