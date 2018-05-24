import pandas as pd
import numpy as np
import pickle
import time
from nltk.tokenize import word_tokenize

df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',dtype = {'food_key':int,'ingredients_list':object}, encoding='ISO-8859-1')


def token_dict_maker(df, text_col_name='food_description'):
	df[text_col_name+'_tokens'] = np.nan
	token_dict = {}
	for i in range(len(df)):
	    token_set = word_tokenize(df[text_col_name].iloc[i])
	    df[text_col_name+'_tokens'].iloc[i] = token_set
	    for token in token_set:
	        if token in token_dict:
	            token_dict[token][0]+= 1
	            token_dict[token][1].append(df['food_key'].iloc[i])
	        else:
	            token_dict[token] = [1, [df['food_key'].iloc[i]]]
	with open('df_token_dict.ojb', 'wb') as file:
	    pickle.dump(token_dict, file)
	return df, token_dict 

food_df, token_dict = token_dict_maker(df)

def one_hot_encoder(df, token_dict):
	
