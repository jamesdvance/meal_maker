
import pandas as pd 
import numpy as np 

fs_all_search = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_groups_in_progress.csv')

#fs_all_search.food_type[fs_all_search.food_type!='restaurant']='grocery'
#fs_all_search = fs_all_search.drop_duplicates()

for i in range(len(fs_all_search.columns)):
    if fs_all_search.iloc[:,i].dtype == 'O' and sum(fs_all_search.iloc[:,i]=='-') > 0:
        print(fs_all_search.columns.values[i])
        print(sum(fs_all_search.iloc[:,i]=='-'))
        fs_all_search.iloc[:,i][fs_all_search.iloc[:,i]=='-'] = 0 
        print(sum(fs_all_search.iloc[:,i]=='-'))


fs_all_search.to_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_groups_formatted.csv', index=False)