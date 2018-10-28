import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re, math
from collections import Counter
import urllib, sys, bs4
from pyshorteners import Shortener
try:
	from .url import fetch_url
except:
	from url import fetch_url
import os
dirpath = os.getcwd()+'/Twitter/'
import requests

class UrlExpand:
	def __init__(self):
		self.shortener = Shortener('Tinyurl')
	def decodeURL(self,url):
		try:
			result = self.shortener.expand(url)
			return result
		except Exception as e:
			return url



def checkAdultContent(dataset):
	adultContentDataset=None
	try:
		adultContentDataset = pd.read_csv(dirpath+'adultcontenturl.csv')
	except:
		adultContentDataset = pd.read_csv('adultcontenturl.csv')
	adultContentDataset = adultContentDataset.iloc[0:3,0].values
	urlExpand = UrlExpand()

	if(len(dataset) == 0):
		return 0
	for data in dataset:
		urls=fetch_url(data)
		for url in urls:
			try:
				r=requests.get(url)
				url=r.url
				if(url=="https://t.co/"):
					continue
				print("checking url : "+url)
				result = urlExpand.decodeURL(url)
				if(result in adultContentDataset):
					#returns 10, if adult content is present
					return 10
			except:
				print("Invalid url")


	#returns 0, if adult content isn't present
	return 0
