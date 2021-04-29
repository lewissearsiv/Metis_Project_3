#Import functions
import streamlit as st
import pandas as pd
from word_finder import *
from sklearn.ensemble import RandomForestClassifier




############################################
#Fit the random Forest classifier for wines#
############################################

binary_features = pd.read_csv('Count_Vec.csv').iloc[:,1:]
target = pd.read_csv('target.csv').iloc[:,1:]

#forest
forest=RandomForestClassifier(n_estimators=100)
forest.fit(binary_features,target)

###################################################################
#Images
from PIL import Image 
french_img  = Image.open('parisian.jpg') 
us_img  = Image.open('CowboyGuy.jpg') 

############################################################################
############################################################################

#Streamlit Functions
    
st.title('What am I drinking?')

st.markdown('### We can help you determine if your chardonnay is from France or the United States.\n ----------------------------')
st.markdown("   ")

client_response = st.text_input('In the most pompous and scientific way possible, describe your chardonnay for me.')

button = st.button('Guess!')
if button: 
    if forest_prediction(client_response, forest) == 'France':
        print( st.image(french_img, use_column_width=True, caption = 'Zis wine is probably from France!'))
    if forest_prediction(client_response, forest) == 'US':
        print( st.image(us_img, use_column_width=True, caption = 'Howdy stranger, this wine must be from right here in America.'))    