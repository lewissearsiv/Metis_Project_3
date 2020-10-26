#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:25:31 2020

@author: lewissears
"""
#################Load in Model and Working Predictor########################
import sys
print("Python Version:", sys.version)
import statistics
import math
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')
from ipynb.fs.full.word_finder_chard import word_finder_matrix
with open('forest_model.pickle','rb') as read_file:
    forest = pickle.load(read_file)   

#Images
from PIL import Image 
french_img  = Image.open('parisian.jpg') 
us_img  = Image.open('CowboyGuy.jpg') 


####################This is the binary identitier###########################
def forest_prediction(description): 
    sample_test_df = pd.DataFrame({'description': [description]})
    word_finder_matrix(sample_test_df)
    if forest.predict([sample_test_df.iloc[0,1:]])[0] == 'France':
        return st.image(french_img, use_column_width=True, caption = 'Zis wine is probably from France!');
        #return 'Zis wine is mozt definitely from France.'
    if forest.predict([sample_test_df.iloc[0,1:]])[0] == 'US':
        return st.image(us_img, use_column_width=True, caption = 'Howdy stranger, this wine must be from right here in America.')
        #return 'Howdy stranger, this wine must be from right here in America.'
############################################################################
    
st.title('What am I drinking?')

st.markdown(' ## We can help you determine if your chardonnay is from France or the United States.')

client_response = st.text_input('In the most pompous and scientific way possible, describe your chardonnay for me.')

button = st.button('Guess!')
if button: 
    st.header(forest_prediction(client_response))


















