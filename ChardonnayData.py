#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setting up the Chardonnay data

@author: lewissears
"""

import sys
print("Python Version:", sys.version)
import statistics
import math
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

###############################################
#This is my random Forest classifier for wines#
###############################################


####################Setup#############################
df_raw_wine = pd.read_csv('Wine_Data/kaggle_wine.csv')
df_wine = df_raw_wine.iloc[:,1:]
df_us = df_wine[df_wine['country'] == 'US']
df_fr = df_wine[df_wine['country'] == 'France']
df_wine2 = pd.concat([df_us, df_fr])
df_wine2.reset_index(drop = True, inplace = True)
df_chard = df_wine2[df_wine2['variety'] == 'Chardonnay']
df_chard.reset_index(drop = True, inplace = True)
from ipynb.fs.full.word_finder_chard import word_finder_matrix
word_finder_matrix(df_chard)
df_chard_us = df_chard[df_chard.country == 'US']
df_chard_fr = df_chard[df_chard.country == 'France']
########################################################

with open('chard_dataframe.pickle', 'wb') as to_write:
    pickle.dump(df_chard, to_write)