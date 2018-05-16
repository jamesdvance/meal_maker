
import pandas as pd
import numpy as np
import tensorflow as tf 


class MealAgent():

# Barebones basic agent - starting with calorie measurement only
	def __init__(self, sess, args): # Args - all measurements- 

		self.sess = sess
		# Arguments
		self.future_steps = np.array(sorted(args['future_steps'])).astype(np.uint32)
		self.meas_to_predict = np.array(args['meas_to_predict']).astype(np.uint32)
		# Stage Measurements 
		self.stage =  # Stage { 1: Breakfast, 2:Lunch, 3: Dinner, 4: Snack}
		self.n_ml_st = # Nth meal in the stage
		self.n_ml_pl = # Nth meal in the full day-play


