# Simple Meal Plan Environment that takes a calorie requirement and iterates on it. 
# Starting simple with this class
import pandas as pd
import numpy as np

class DayPlan():
    
    def __init__(self):
        # Nutrition DataFrame
        self.df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',dtype = {'food_key':int,'ingredients_list':object}, encoding='ISO-8859-1')
        self.df = self.df.fillna(0)
        self.plan_df = pd.DataFrame(columns=self.df.columns.values)
        self.s=0
        self.r=0

    # Short  & Long Term Payoff
    def set_num_reqs(self, num_reqs_df):
        self.cal_req = num_reqs_df['calories'].item()
        self.mac_mat = num_reqs_df[['protein_g', 'carb_g','fat_g']].as_matrix()
        self.req_mat = num_reqs_df[['fiber_g','calcium_mg','iron_mg','vit_a_mcg','vit_c_mg']].as_matrix()
        self.thr_mat= num_reqs_df[['saturated_fat_g', 'sodium_mg','cholesterol_mg']].as_matrix()
        self.req_names = num_reqs_df.columns.values
    
    def reset(self):
        self.plan_df = pd.DataFrame(columns=self.df.columns.values)
        
        self.s = 0
        self.r = 0

    
    # Long term, it needs to not just randomly select states, but to evaluate based on the nutrient profile of each food
    def step(self, plan_vec):
        # Plan vec should be [1,len(df)] vector to select 1 food item
        add_df = self.df[list(map(bool, list(plan_vec)))]
        self.plan_df = self.plan_df.append([add_df], ignore_index=True)
        # Aggregate to single row
        self.agg_pl = pd.DataFrame([list(map(lambda x: sum(self.plan_df[x]),self.req_names))], columns=self.req_names)
        # additional reward
        a =0
        if (sum(self.plan_df['calories']) > (self.cal_req - 75)) and (sum(self.plan_df['calories']) < (self.cal_req+75)):
            d = True
            if self.s < 3:
                a-=100               
            else:
                a +=1000 # Successful meal plan 
        elif sum(self.plan_df['calories']) > (self.cal_req+75):
            d = True
            a -=100
        # Plan can include no more than 15 foods
        elif self.s > 14:
            d = True

        else: 
            d = False
        
        # Can have different rewards on either side of 15. 
        # Need to normalize 
        # Negative cost function probably not going to work here since its additive (??)
        
        mac_c = -1*np.sum(np.sqrt((self.agg_pl[['protein_g', 'carb_g','fat_g']].as_matrix().astype(float) - self.mac_mat)**2))*5
        req_c = -1*np.sum(np.sqrt((self.agg_pl[['fiber_g','calcium_mg','iron_mg','vit_a_mcg','vit_c_mg']].as_matrix().astype(float)-self.req_mat)**2)) *0.5
        # Need to normalize below
        thresh_c = -1*np.sum(np.minimum(self.thr_mat-self.agg_pl[['saturated_fat_g', 'sodium_mg','cholesterol_mg']].as_matrix().astype(float), np.zeros(len(self.thr_mat)))) *0.5

        '''
        mac_c = 1/(np.sum(np.sqrt((self.agg_pl[['protein_g', 'carb_g','fat_g']].as_matrix().astype(float) - self.mac_mat)**2))*5)
        req_c = 1/(np.sum(np.sqrt((self.agg_pl[['fiber_g','calcium_mg','iron_mg','vit_a_mcg','vit_c_mg']].as_matrix().astype(float)-self.req_mat)**2)) *0.5)
        thresh_c = 1/(np.sum(np.minimum(self.thr_mat-self.agg_pl[['saturated_fat_g', 'sodium_mg','cholesterol_mg']].as_matrix().astype(float), np.zeros(len(self.thr_mat)))) *0.5)
        '''

        # Total Cost
        self.r = sum([mac_c, req_c, thresh_c, a])
        self.s +=1
        return self.s, self.r, d
        
    # Short term food_type_grp categor
    '''
    def set_food_type_grp(self):
        
    # Get current state and add food at state+1
    # Should allow state to remain at zero and advance to next stage
    # Instead, shouldn't there be 4 stages, Breakfast, Lunch, Dinner, Snacks. Each can have 1-5 items
    # Then this becomes a three-dimensional problem - Meals, N Stages Per Meal, Which Vec Per Meal
    # S is the current state vector
    def step(self,s,a):
        
        
        
    def reset(self):
        
    def render():
    '''
    