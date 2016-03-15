#!/usr/bin/python
# -*- coding: utf-8 -*-


import os 
import numpy as np
from pylab import *
import csv

#import utils

import matplotlib.pyplot as plt
import pandas as pd


import json
import csv
import gc
from pandas import read_csv


#from os import walk
import os.path 

df=pd.read_csv('fapesp.csv')



import os, sys
sys.path.append("../pylinguistics/pylinguistics/")

import Pylinguistics as pl
count=0
def calcLinguistic(x):
    global count
    print('%i/%i'%(count,len(df)))
    count+=1
    objpl=pl.text(str(x).decode('utf-8'))
    objpl.setLanguage("pt");
    print(objpl.getFeatures())
    return objpl

bm = df.texto.map(calcLinguistic)

features = []
features = [ i.getFeatures() for i in bm ]

dataFeatures = pd.DataFrame(features)
dataFeatures.to_csv('fapesp_features.csv',encoding='utf-8')
