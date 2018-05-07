


import pandas as pd 
import numpy as np 

df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_all_search_progress.csv')

# Python reads '-' as zeros, sql isn't. (B/C SQL in UTF-8?)

for i in range(len(df.columns)):
    if df.iloc[:,i].dtype == 'O' and sum(df.iloc[:,i]=='-') > 0:
        fs_all_search[fs_all_search.iloc[:,i]=='-'] = 0 

