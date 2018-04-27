import cvxpy
import pandas as pd
import numpy as np
import pickle


df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv',  encoding='ISO-8859-1')

num_reqs_df = pd.read_csv("../desktop-meal-maker/num_reqs_df.csv")

df['p_accept'] = .5 + np.random.rand(len(df),1)*.01


#meals_df=df[df.food_type_grp=='grocery']
meals_df=df[df.food_type_grp=='grocery']
del df
reqs_df = num_reqs_df
oth_relax = .01
P = 10
mac_relax=0.03


x = cvxpy.Bool(len(meals_df))

m = meals_df['p_accept'].as_matrix().astype(float) # p(acceptance)
    # Setting constraint variables
c = meals_df['carb_g'].as_matrix().astype(float) # carbs
f = meals_df['fat_g'].as_matrix().astype(float) # fat
p = meals_df['protein_g'].as_matrix().astype(float) # protein
'''
ca = meals_df['calcium_mg'].as_matrix() # calcium
i = meals_df['iron_mg'].as_matrix() # iron
s = meals_df['sodium_mg'].as_matrix() # sodium
v_a = meals_df['vit_a_mcg'].as_matrix() # vitamin A
v_c = meals_df['vit_c_mg'].as_matrix() # vitamin C
ch = meals_df['cholesterol_mg'].as_matrix() # cholesterol
f = meals_df['fiber_g'].as_matrix() # fiber
sa = meals_df['saturated_fat_g'].as_matrix() # saturated fat
su = meals_df['sugar_g'].as_matrix() # sugar_g
'''

items = np.ones(len(meals_df))


constraints = [
        items*x <= P, # no more than P items
        cvxpy.abs(sum(c*x) - reqs_df['carb_g'].item()) < reqs_df['carb_g'].item()*mac_relax,# within 5% of requirements
        cvxpy.abs(sum(f*x) - reqs_df['fat_g'].item()) < reqs_df['fat_g'].item()*mac_relax,
        cvxpy.abs(sum(p*x) - reqs_df['protein_g'].item()) < reqs_df['protein_g'].item()*mac_relax
        #abs(sum(x*ca) - reqs_df['calcium_mg'].item()) < reqs_df['calcium_mg'].item()*oth_relax,
        #abs(sum(x*i) - reqs_df['iron_mg'].item()) < reqs_df['iron_mg'].item()*oth_relax,
        #cvxpy.sum_entries(x)
        #s*x - reqs_df['sodium_mg'].item() < reqs_df['sodium_mg'].item()*oth_relax,# just above zero
        #abs(sum(x*v_a) - reqs_df['vit_a_mcg'].item()) < reqs_df['vit_a_mcg'].item()*oth_relax,
        #abs(sum(x*v_c) - reqs_df['vit_c_mg'].item()) < reqs_df['vit_c_mcg'].item()*oth_relax,
        #sum(x*ch) - reqs_df['cholesterol_mg'].item() < reqs_df['cholesterol_mg'].item()*oth_relax,
        #abs(sum(x*f) - reqs_df['fiber_g'].item()) < reqs_df['fiber_g'].item()*oth_relax,
        #sum(x*f) - reqs_df['saturated_fat_g'].item() < reqs_df['saturated_fat_g'].item()*oth_relax,
        #sum(x*f) - reqs_df['sugar_g'].item() < reqs_df['sugar_g'].item()*oth_relax
]


prob = cvxpy.Problem(cvxpy.Maximize(m*x), constraints)

prob.solve(verbose=True, solver= 'GLPK_MI')

df_ind = pd.DataFrame(x.value, columns=['ind'])
meals_df = pd.concat([meals_df, df_ind], axis=1)
plan_df = meals_df[meals_df.ind==1]

plan_df.to_csv("plan_df.csv", axis=False)