import pandas as pd 
import numpy as np 
from unidecode import unidecode

diet_facts_df = pd.read_csv("C:/Users/J/Desktop/Businesses/Meal_Maker/diet_facts_brand_foods_in_progress.csv")

restaurants_df = pd.read_csv("C:/Users/J/Desktop/Businesses/Meal_Maker/restaurant_foods_in_progress.csv", encoding = 'utf-8')

def format_perc(x):
    if type(x)!=str:
        return x
    elif len(x) >6:
        return np.nan
    else:
        return x.replace('%',u'').replace('<',u'')

def strip_g(x):
    if type(x) != str:
        return x
    else:
        return float(x.replace('g',u'').replace('<',u''))

def strip_mg(x):
    if type(x) != str:
        return x
    else:
        return float(x.replace('mg',u'').replace('<',u''))

def category_finder(x):
    if x in other_brands:
        return 'brand'
    else:
        return 'restaurant'

def unencode(x):
    if type(x) != str:
        return x
    else:
        return unidecode(x)

# Strip percentages
diet_facts_df['calcium_perc'] = diet_facts_df['calcium_perc'].map(lambda x: format_perc(x))
diet_facts_df['iron_perc'] = diet_facts_df['iron_perc'].map(lambda x: format_perc(x))
diet_facts_df['vit_a_perc'] = diet_facts_df['vit_a_perc'].map(lambda x: format_perc(x))
diet_facts_df['vit_c_perc'] = diet_facts_df['vit_c_perc'].map(lambda x: format_perc(x))
# Strip grams
diet_facts_df['carb_g'] = diet_facts_df['carb_g'].map(lambda x: strip_g(x))
diet_facts_df['fat_g'] = diet_facts_df['fat_g'].map(lambda x: strip_g(x))
diet_facts_df['fiber_g'] = diet_facts_df['fiber_g'].map(lambda x: strip_g(x))
diet_facts_df['protein_g'] = diet_facts_df['protein_g'].map(lambda x: strip_g(x))
diet_facts_df['saturated_fat_g'] = diet_facts_df['saturated_fat_g'].map(lambda x: strip_g(x))
diet_facts_df['sugar_g'] = diet_facts_df['sugar_g'].map(lambda x: strip_g(x))
diet_facts_df['trans_fat_g'] = diet_facts_df['trans_fat_g'].map(lambda x: strip_g(x))
# Strip milligrams
diet_facts_df['cholesterol_mg'] = diet_facts_df['cholesterol_mg'].map(lambda x: strip_mg(x))
diet_facts_df['potassium_mg'] = diet_facts_df['potassium_mg'].map(lambda x: strip_mg(x))
diet_facts_df['sodium_mg'] = diet_facts_df['sodium_mg'].map(lambda x: strip_mg(x))
diet_facts_df['calories'] = diet_facts_df['calories'].map(lambda x: strip_mg(x))
diet_facts_df['brand_name'] = diet_facts_df['brand_name'].map(lambda x: unencode(x))
diet_facts_df['serving_size'] = diet_facts_df['serving_size'].map(lambda x: unencode(x))
diet_facts_df['item_name'] = diet_facts_df['item_name'].map(lambda x: unencode(x))
diet_facts_df['item_desc'] = diet_facts_df['item_desc'].map(lambda x: unencode(x))
diet_facts_df['brand_label'] = diet_facts_df['brand_label'].map(lambda x: unencode(x))
# Seperating into restaurants vs brandsrestaurant_brands = rest_df.brand_label.unique()
restaurant_brands = restaurants_df.brand_label.unique()
all_brands = diet_facts_df.brand_label.unique()
other_brands = set(all_brands) - set(restaurant_brands)
diet_facts_df['category'] = diet_facts_df.brand_label.map(lambda x: category_finder(x))

diet_facts_df.to_csv("C:/Users/J/Desktop/Businesses/Meal_Maker/diet_facts_df_formatted.csv", index=False, encoding='utf-8')
