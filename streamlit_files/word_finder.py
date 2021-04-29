#Here are some functions to pull words from descriptions
#To be used in US_vs_French_Wine Classifier system
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
def oak_finder(description):
    string = description.lower()
    num = string.find(' oak')
    numneg1 = string.find('no oak')
    numneg2 = string.find('unoak')
    numneg3 = string.find('not oak')
    if num == -1:
        return 0
    elif numneg1 != -1:
        return 0
    elif numneg2 != -1:
        return 0
    elif numneg3 != -1:
        return 0
    else: 
        return 1
def wood_finder(description):
    string = description.lower()
    num = string.find('wood')
    numneg = string.find('no wood')
    if num == -1 or numneg != -1:
        return 0
    else: 
        return 1
def tannin_finder(description):
    string = description.lower()
    num = string.find('tannin')
    numneg = string.find('no tannin')
    if num == -1 or numneg != -1:
        return 0
    else: 
        return 1
def metal_finder(description):
    string = description.lower()
    num = string.find('metal')
    if num == -1:
        return 0
    else: 
        return 1
def steel_finder(description):
    string = description.lower()
    num = string.find('steel')
    if num == -1:
        return 0
    else: 
        return 1      
def spice_finder(description):
    string = description.lower()
    num = string.find('spice')
    num2 = string.find('spicy')
    if num == -1 and  num2 == -1:
        return 0
    else: 
        return 1
def butter_finder(description):
    string = description.lower()
    num = string.find('butter')
    numneg = string.find('no butter')
    if num == -1 or numneg!= -1:
        return 0
    else: 
        return 1
def cream_finder(description):
    string = description.lower()
    num = string.find('cream')
    if num == -1:
        return 0
    else: 
        return 1   
def mineral_finder(description):
    string = description.lower()
    num = string.find('mineral')
    if num == -1:
        return 0
    else: 
        return 1
def limestone_finder(description):
    string = description.lower()
    num = string.find('stone')
    if num == -1:
        return 0
    else: 
        return 1
def chalk_finder(description):
    string = description.lower()
    num = string.find('chalk')
    if num == -1:
        return 0
    else: 
        return 1
def citrus_finder(description):
    string = description.lower()
    num = string.find('citrus')
    numneg = string.find('no citrus')
    if num == -1 or numneg != -1:
        return 0
    else: 
        return 1
def lemon_finder(description):
    string = description.lower()
    num2 = string.find('lemon')
    if num2 == -1:
        return 0
    else: 
        return 1
def orange_finder(description):
    string = description.lower()
    num2 = string.find('orange')
    if num2 == -1:
        return 0
    else: 
        return 1
def floral_finder(description):
    string = description.lower()
    num2 = string.find('floral')
    if num2 == -1:
        return 0
    else: 
        return 1
def acidic_finder(description):
    string = description.lower()
    num = string.find('acidic')
    num2 = string.find('acidity')
    numneg = string.find('no acid')
    if num == -1 and num2 == -1:
        return 0
    elif numneg != -1:
        return 0
    else: 
        return 1
def bold_finder(description):
    string = description.lower()
    num = string.find('bold')
    num2 = string.find('big')
    if num == -1 and num2 == -1:
        return 0
    else: 
        return 1
def rich_finder(description):
    string = description.lower()
    num = string.find('rich')
    if num == -1:
        return 0
    else: 
        return 1
def subtle_finder(description):
    string = description.lower()
    num = string.find('subtle')
    if num == -1:
        return 0
    else: 
        return 1
def light_finder(description):
    string = description.lower()
    num = string.find('light')
    if num == -1:
        return 0
    else: 
        return 1
def gentle_finder(description):
    string = description.lower()
    num = string.find('gentle')
    if num == -1:
        return 0
    else: 
        return 1
def fruit_finder(description):
    string = description.lower()
    num = string.find('fruit')
    numneg = string.find('no fruit')
    if num == -1 or numneg != -1:
        return 0
    else: 
        return 1
def earth_finder(description):
    string = description.lower()
    num = string.find('earth')
    if num == -1:
        return 0
    else: 
        return 1
def dirt_finder(description):
    string = description.lower()
    num = string.find('dirt')
    if num == -1:
        return 0
    else: 
        return 1
def ripe_finder(description):
    string = description.lower()
    num = string.find('ripe')
    if num == -1:
        return 0
    else: 
        return 1
def smoke_finder(description):
    string = description.lower()
    num = string.find('smoke')
    if num == -1:
        return 0
    else: 
        return 1
def apple_finder(description):
    string = description.lower()
    num = string.find('apple')
    if num == -1:
        return 0
    else: 
        return 1
def pear_finder(description):
    string = description.lower()
    num = string.find('pear')
    if num == -1:
        return 0
    else: 
        return 1
def nut_finder(description):
    string = description.lower()
    num = string.find('nut')
    if num == -1:
        return 0
    else: 
        return 1
def petrol_finder(description):
    string = description.lower()
    num = string.find('petrol')
    if num == -1:
        return 0
    else: 
        return 1
def caramel_finder(description):
    string = description.lower()
    num = string.find('caramel')
    if num == -1:
        return 0
    else: 
        return 1
def vanilla_finder(description):
    string = description.lower()
    num = string.find('vanilla')
    if num == -1:
        return 0
    else: 
        return 1
def tobacco_finder(description):
    string = description.lower()
    num = string.find('tobacco')
    if num == -1:
        return 0
    else: 
        return 1
def leather_finder(description):
    string = description.lower()
    num = string.find('leather')
    if num == -1:
        return 0
    else: 
        return 1
def cheese_finder(description):
    string = description.lower()
    num = string.find('cheese')
    num2 = string.find('rind')
    if num == -1 and num2 == -1:
        return 0
    else: 
        return 1
def coconut_finder(description):
    string = description.lower()
    num = string.find('coconut')
    if num == -1:
        return 0
    else: 
        return 1
def salt_finder(description):
    string = description.lower()
    num = string.find('salt')
    num2 = string.find('salinity')
    if num == -1 and num2 == -1:
        return 0
    else: 
        return 1
def crisp_finder(description):
    string = description.lower()
    num = string.find('crisp')
    if num == -1:
        return 0
    else: 
        return 1
def clean_finder(description):
    string = description.lower()
    num = string.find('clean')
    if num == -1:
        return 0
    else: 
        return 1
def tropical_finder(description):
    string = description.lower()
    num = string.find('tropical')
    if num == -1:
        return 0
    else: 
        return 1
def baking_spices_finder(description):
    string = description.lower()
    num = string.find('baking spices')
    if num == -1:
        return 0
    else: 
        return 1
def cinnamon_finder(description):
    string = description.lower()
    num = string.find('cinnamon')
    if num == -1:
        return 0
    else: 
        return 1
def nutmeg_finder(description):
    string = description.lower()
    num = string.find('nutmeg')
    if num == -1:
        return 0
    else: 
        return 1
def peach_finder(description):
    string = description.lower()
    num = string.find('peach')
    if num == -1:
        return 0
    else: 
        return 1
def pineapple_finder(description):
    string = description.lower()
    num = string.find('pineapple')
    if num == -1:
        return 0
    else: 
        return 1
def papaya_finder(description):
    string = description.lower()
    num = string.find('papaya')
    if num == -1:
        return 0
    else: 
        return 1
def sharp_finder(description):
    string = description.lower()
    num = string.find('sharp')
    if num == -1:
        return 0
    else: 
        return 1
def dull_finder(description):
    string = description.lower()
    num = string.find('dull')
    if num == -1:
        return 0
    else: 
        return 1
def grass_finder(description):
    string = description.lower()
    num = string.find('grass')
    if num == -1:
        return 0
    else: 
        return 1
def licorice_finder(description):
    string = description.lower()
    num = string.find('licorice')
    if num == -1:
        return 0
    else: 
        return 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def word_finder_matrix(df_chard):
    df_chard['oak'] = df_chard['description'].apply(oak_finder)
    df_chard['wood'] = df_chard['description'].apply(wood_finder)
    df_chard['tannin'] = df_chard['description'].apply(tannin_finder)
    df_chard['metal'] = df_chard['description'].apply(metal_finder)
    df_chard['steel'] = df_chard['description'].apply(steel_finder)
    df_chard['spice'] = df_chard['description'].apply(spice_finder)
    df_chard['butter'] = df_chard['description'].apply(butter_finder)
    df_chard['cream'] = df_chard['description'].apply(cream_finder)
    df_chard['mineral'] = df_chard['description'].apply(mineral_finder)
    df_chard['limestone'] = df_chard['description'].apply(limestone_finder)
    df_chard['chalk'] = df_chard['description'].apply(chalk_finder)
    df_chard['citrus'] = df_chard['description'].apply(citrus_finder)
    df_chard['lemon'] = df_chard['description'].apply(lemon_finder)
    df_chard['orange'] = df_chard['description'].apply(orange_finder)
    df_chard['floral'] = df_chard['description'].apply(floral_finder)
    df_chard['acidic'] = df_chard['description'].apply(acidic_finder)
    df_chard['bold'] = df_chard['description'].apply(bold_finder)
    df_chard['rich'] = df_chard['description'].apply(rich_finder)
    df_chard['subtle'] = df_chard['description'].apply(subtle_finder)
    df_chard['light'] = df_chard['description'].apply(light_finder)
    df_chard['gentle'] = df_chard['description'].apply(gentle_finder)
    df_chard['fruit'] = df_chard['description'].apply(fruit_finder)
    df_chard['earth'] = df_chard['description'].apply(earth_finder)
    df_chard['dirt'] = df_chard['description'].apply(dirt_finder)
    df_chard['ripe'] = df_chard['description'].apply(ripe_finder)
    df_chard['smoke'] = df_chard['description'].apply(smoke_finder)
    df_chard['apple'] = df_chard['description'].apply(apple_finder)
    df_chard['pear'] = df_chard['description'].apply(pear_finder)
    df_chard['nut'] = df_chard['description'].apply(nut_finder)
    df_chard['petrol'] = df_chard['description'].apply(petrol_finder)
    df_chard['caramel'] = df_chard['description'].apply(caramel_finder)
    df_chard['vanilla'] = df_chard['description'].apply(vanilla_finder)
    df_chard['tobacco'] = df_chard['description'].apply(tobacco_finder)
    df_chard['leather'] = df_chard['description'].apply(leather_finder)
    df_chard['cheese'] = df_chard['description'].apply(cheese_finder)
    df_chard['coconut'] = df_chard['description'].apply(coconut_finder)
    df_chard['salt'] = df_chard['description'].apply(salt_finder)
    df_chard['crisp'] = df_chard['description'].apply(crisp_finder)
    df_chard['clean'] = df_chard['description'].apply(clean_finder)
    df_chard['tropical'] = df_chard['description'].apply(tropical_finder)
    df_chard['baking spices'] = df_chard['description'].apply(baking_spices_finder)
    df_chard['cinnamon'] = df_chard['description'].apply(cinnamon_finder)
    df_chard['nutmeg'] = df_chard['description'].apply(nutmeg_finder)
    df_chard['peach'] = df_chard['description'].apply(nutmeg_finder)
    df_chard['pineapple'] = df_chard['description'].apply(pineapple_finder)
    df_chard['papaya'] = df_chard['description'].apply(papaya_finder)
    df_chard['sharp'] = df_chard['description'].apply(sharp_finder)
    df_chard['dull'] = df_chard['description'].apply(dull_finder)
    df_chard['grass'] = df_chard['description'].apply(grass_finder)
    df_chard['licorice'] = df_chard['description'].apply(licorice_finder)

#This gives a prediction
def forest_prediction(description, forest): 
    sample_test_df = pd.DataFrame({'description': [description]})
    word_finder_matrix(sample_test_df)
    return forest.predict([sample_test_df.iloc[0,1:]])[0]