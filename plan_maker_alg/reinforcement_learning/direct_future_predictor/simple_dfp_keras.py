import pandas as pd 
import numpy as np 
import tensorflow as tf 

# Load in starting data
df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',dtype = {'food_key':int,'ingredients_list':object}, encoding='ISO-8859-1')
df = df.fillna(0)
nut_mat= df[['calories','protein_g', 'fat_g','saturated_fat_g', 'carb_g', 'fiber_g', 'sugar_g', 'sodium_mg', 'cholesterol_mg', 'calcium_mg', 'iron_mg', 'vit_a_mcg', 'vit_c_mg']].as_matrix()

# Initialize init_state variable here - can be all zeros, or come from a partially created meal plan 
init_state = np.zeros(nut_mat.shape[1])


#
#          Graph Architexture            
#

''' 
Perception

# Perception model happens at time 0 for an action, Measurement module starts at time 1 and beyond 
'''
state_input = df.keras.Input(init_state)


'''
Measurement

# Change in state
'''

state_a1 = 



'''
Goal

'''



