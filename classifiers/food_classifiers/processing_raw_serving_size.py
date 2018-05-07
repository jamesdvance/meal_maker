

import pandas as pd 
from fractions import Fraction 

df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_2018_3_15_processed_comma.csv', delimiter = ',',encoding='ISO-8859-1')

def process_ss(df):
	df['serving_size_raw'] = df['serving_size_raw'].fillna('1 item')
	for i in range((len(df.serving_size_raw))):
	    line_strings = []
	    line_floats = []
	    float_strs = []
	    frac_orig = 0
	    line = df.iloc[i,6]
	    if type(line) == str:
	        for t in line.split():
	        ##### Splits All Into Strings and Floats 
	            try:
	                float(t)
	                line_floats.append(float(t))
	                float_strs.append(t)
	            except ValueError:
	                try: 
	                    float(Fraction(t))
	                    line_floats.append(float(Fraction(t)))
	                    float_strs.append(t)
	                except ValueError:
	                    line_strings.append(t)
	        ##### If more than 1 value, set first value to unit, and set unit to the string between that value and the next value
	        if len(line_floats) > 1:
	            df.serving_size_val.iloc[i] = line_floats[0]
	            # This way it doesn't seperate 'fl and 'oz'
	            text1 = line[(line.find(float_strs[0])+len(float_strs[0])):(line.find(float_strs[1])-1)].strip()
	            df.serving_size_unit.iloc[i] = text1
	        ##### If
	        elif len(line_floats) == 1:
	            df.serving_size_val.iloc[i] = line_floats[0] # 
	            df.serving_size_unit.iloc[i] = line[(line.find(float_strs[0])+len(float_strs[0])):len(line)].strip()
	        ##### Empty line floats - set value to 1 and unit to the full string
	        else:
	            df.serving_size_val.iloc[i] = 1
	            df.serving_size_unit.iloc[i] = line
	    else:
	        #################
	        #     df is a single number or non-string
	        #################
	        df.serving_size_val.iloc[i] = line
	return df

df = process_ss(df)

df.to_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv')