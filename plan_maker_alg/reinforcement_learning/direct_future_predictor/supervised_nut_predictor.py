

# Predicts The Nutritional Change In some state by selecting 1 - 450k. 



import tensorflow as tf 
import numpy as np
import pandas as pd
## simple feed-forward neural network to predict how many calories given the action, and then to select an action based on a calorie goal
#################################
#     Data
#################################
df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',dtype = {'food_key':int,'ingredients_list':object}, encoding='ISO-8859-1')
df = df.fillna(0)
nut_mat= df[['calories','protein_g', 'fat_g','saturated_fat_g', 'carb_g', 'fiber_g', 'sugar_g', 'sodium_mg', 'cholesterol_mg', 'calcium_mg', 'iron_mg', 'vit_a_mcg', 'vit_c_mg']].as_matrix()



################################
#    Parameters
################################
# SGD or GD learning rate i.e. step size

################################
#    Variables - moving away from the exact Doom DFP architecture
################################
selector = tf.zeros(shape=nut_mat.shape[1], name ="Selector")

################################
#    Model Structure
################################


################################
#    Layers
################################


#################################
#     Model Structures
#################################
## Hidden Layer


## Against Calories
################################
#    Adding to Tensorboard
################################


################################
#    Running Session
################################

################################
#    Running Session
################################
