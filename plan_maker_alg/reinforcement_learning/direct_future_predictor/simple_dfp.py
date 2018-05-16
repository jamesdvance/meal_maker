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
'''
If more measurements are better, can also include other metadata about the situation and predictions, such as accuracy of previous ma2 prediction, distance between prev and new choices, etc
The hope is that predictions are better with a nearer measurement timestep (becoming percent at timestep t) but it also learns how to predict the affect of current action t on given meal m
'''
# Init Measurement
# Action Choice a1
# Measurement ma11
# Action Choice a2
# Measurement ma12, ma21
# Action Choice a3
# Measurement ma13, ma22, ma31
# Action Choice a4
# Measurement ma14, ma23, ma32, ma41
# Outputs Nutrient Prediction - a1 - > ma1, ma2, ma3, ma4
# Measurement

# Each action a has predicted impact matrix with each measurement (13 nutritional) and each expected timestep 1 - 4
# 450k x 13 x 15 = 87M predictions

# What it should really do is take in a measurement and a goal and output a prediction for how close it will get to that goal. Then learn what that closeness means.



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
