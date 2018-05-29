import pandas as pd
import numpy as np
import pickle
import time
from nltk.tokenize import word_tokenize
#from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import string

df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',dtype = {'food_key':int,'ingredients_list':object}, encoding='ISO-8859-1')


def token_dict_maker(df, text_col_name='food_description'):
    token_dict = {}
    df['food_desc_tokens'] = np.nan
    for i in range(len(df)):
    # Tokenize words
        token_set = word_tokenize(df.food_description.iloc[i])
	    # Remove Punctuation
        token_set = [i for i in token_set if i not in string.punctuation]
	    # Lowercase words
        token_set = list(map(lambda x: x.lower(), token_set))
	    # Exclude Stopwords
        token_set = [i for i in token_set if i not in stopwords.words('english')]
	    # Stem Words
        token_set = [SnowballStemmer('english').stem(i) for i in token_set]
        df['food_desc_tokens'].iloc[i] = token_set
        for token in token_set:
            if token in token_dict:
                token_dict[token][0]+= 1
                token_dict[token][1].append(df['food_key'].iloc[i])
            else:
                token_dict[token] = [1, [df['food_key'].iloc[i]]]
    return df, token_dict


def bigram_dict_maker(df, text_col_name='food_description'):
 	 bigram_dict = []
     return df, bigram_dict


# Can enter a token_dict filtered by n total items
def one_hot_encoder(df, token_dict):
    fd_key_df = df[['food_key','food_description']]
    for key, value in token_dict.items():
        ohe_df = pd.DataFrame({'food_key':value[1], 'encoding':list(np.ones(len(value[1])))})
        fd_key_df = fd_key_df.merge(ohe_df,how='left', on='food_key')
        fd_key_df['encoding'] = fd_key_df['encoding'].fillna(0)
        fd_key_df.columns = list(fd_key_df.columns.values)[0:(len(fd_key_df.columns.values)-1)]+[key]
    return fd_key_df

test_df = df.iloc[0:50, :]

food_df, token_dict = token_dict_maker(test_df)

new_df = one_hot_encoder(food_df, token_dict)

new_df.to_csv("ohe_test_results.csv",index=False)