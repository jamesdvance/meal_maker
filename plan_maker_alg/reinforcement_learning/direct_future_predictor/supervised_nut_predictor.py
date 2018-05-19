

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

goal_arr = pd.read_csv('C:/Users/J/Fitness/Meal Plans/num_reqs_df.csv').as_matrix()

################################
#    Variables - moving away from the exact Doom DFP architecture
################################
nut_data = tf.placeholder(tf.float32, shape=nut_mat.shape)

selector = tf.Variable(shape=nut_mat.shape[1], name ="Selector")


################################
#    Parameters
################################
# SGD or GD learning rate i.e. step size
step_size = 0.01
# Epochs - number of times the data goes through a network and is backpropogated back through
epochs = 1000
# Batch Size - number of training examples per batch (different than number of batches)
# Iterations - number of batches needed to complete one epoch
# If there are 2000 training examples, and Batch Size = 500, it will take 4 iterations to complete 1 epoch
################################
#    Model Structure
################################
# Max 


# Selector 0 times 1 equals first meal
# Mutliplies a 13 x 450k vector by a 450k x 1 vector and outputs a 13 x 1 vector
prod_1 = tf.matmul(nut_data, selector)

#prod_2 = tf.matmul(nut_data, selector)

################################
#    Layers
################################
# Computes loss on 13 x 1 prod1 and 13 x 1 goal vec
se_loss = tf.square(prod1-goal_arr)

opt = tf.train.GradientDescentOptimizer(step_size).minimize(se_loss)

# Loss function should be the result of going to 


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
for i in range(epochs):


################################
#    Running Session
################################
