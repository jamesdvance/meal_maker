import pandas as pd
import numpy as np
from random import randint
import math

prot_req = 144
fat_req = 64
carb_req = 132

full_df = pd.read_csv("C:/Users/J/Desktop/Businesses/branded_foods_in_progress.csv")

alpha_df = full_df[['ndb_no','desc_only','kilocalories', 'protein_g','fat_g','carb_g','unit_per_item']]
useful_df = alpha_df[alpha_df['kilocalories']>0]

useful_df.protein_g[useful_df['protein_g'].isnull()] = 0
useful_df.fat_g[useful_df['fat_g'].isnull()] = 0
useful_df.carb_g[useful_df['carb_g'].isnull()] = 0
useful_df.isnull().sum()
useful_df.protein_g = useful_df.protein_g.astype(int)
useful_df.fat_g = useful_df.fat_g.astype(int)
useful_df.carb_g = useful_df.carb_g.astype(int)

useful_df['prot_prop'] = useful_df.protein_g/(useful_df.protein_g+useful_df.fat_g+useful_df.carb_g)
useful_df['fat_prop'] = useful_df.fat_g/(useful_df.protein_g+useful_df.fat_g+useful_df.carb_g)
useful_df['carb_prop'] = useful_df.carb_g/(useful_df.protein_g+useful_df.fat_g+useful_df.carb_g)

useful_df.to_csv('C:/Users/J/Datasets/useful_nutrition_df.csv',index=False)


# test case
# Calculate proportions of final requirements
def meal_maker2(prot_req, fat_req, carb_req):
    # Proportions of initial requirements
    proportions = np.array([prot_req/sum([prot_req,fat_req,carb_req]),fat_req/sum([prot_req,fat_req,carb_req]),carb_req/sum([prot_req,fat_req,carb_req])])
    # Sort full df by distance to initial proportions
    useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)
    #temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)-1),:])
    useful_df = useful_df.sort_values(by=['prop_distance'])
    plan_df = pd.DataFrame([useful_df.iloc[1,:]])
    useful_df = useful_df.drop(useful_df.index[[0]])
    delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])

    while sum((abs(delta)<np.array([0.05*prot_req,0.05*fat_req,0.05*carb_req])))!=3:
# This part could be parallelized: Split into groups, calculate distance at the same time then bring together with merge sort
        delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])
        proportions = np.array([delta[0]/sum(delta),delta[1]/sum(delta),delta[2]/sum(delta)])
# Calculate new distance and new sort
        useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)# a
        useful_df = useful_df.sort_values(by=['prop_distance'])
# Append closest distance
        plan_df = plan_df.append([useful_df.iloc[1,:]],ignore_index=True)
# Calculate new delta
        print(delta)
        print(proportions)
    return plan_df

proportions = np.array([prot_req/sum([prot_req,fat_req,carb_req]),fat_req/sum([prot_req,fat_req,carb_req]),carb_req/sum([prot_req,fat_req,carb_req])])
    # Sort full df by distance to initial proportions
useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)
    #temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)-1),:])
useful_df = useful_df.sort_values(by=['prop_distance'])
plan_df = pd.DataFrame([useful_df.iloc[0,:]])
useful_df = useful_df.drop(useful_df.index[[0]])
delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])

while sum((abs(delta)<np.array([0.05*prot_req,0.05*fat_req,0.05*carb_req])))!=3 and sum(delta<0)<3:
# This part could be parallelized: Split into groups, calculate distance at the same time then bring together with merge sort
    delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])
    proportions = np.array([delta[0]/sum(delta),delta[1]/sum(delta),delta[2]/sum(delta)])
# Calculate new distance and new sort
    useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)# a
    useful_df = useful_df.sort_values(by=['prop_distance'])
# Append closest distance
    plan_df = plan_df.append([useful_df.iloc[0,:]],ignore_index=True)
# Drop used
    useful_df = useful_df.drop(useful_df.index[[0]])
# Calculate new delta
    print(delta)
    print(proportions)


plan_df.to_csv('first_meal_plan.csv')