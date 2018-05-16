import pandas as pd
import numpy as np
from random import randint
import math


useful_df = pd.read_csv('C:/Users/J/Datasets/useful_nutrition_df.csv', encoding ='ISO-8859-1')
# Randomly assign groups 1 - 5. 
useful_df['rand_group'] = [randint(0,4) for i in range(len(useful_df))]
# Rules: Need 1 from each group.
prot_req = 144
fat_req = 64
carb_req = 132

def add_sorted_item(useful_df, plan_df, delta, proportions):
    delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])
    proportions = np.array([delta[0]/sum(delta),delta[1]/sum(delta),delta[2]/sum(delta)])
    useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)# a
    useful_df = useful_df.sort_values(by=['prop_distance'])
# Append closest distance
    plan_df = plan_df.append([useful_df.iloc[0,:]],ignore_index=True)
# Drop used
    useful_df = useful_df.drop(useful_df.index[[0]])

    return plan_df, delta, proportions

proportions = np.array([prot_req/sum([prot_req,fat_req,carb_req]),fat_req/sum([prot_req,fat_req,carb_req]),carb_req/sum([prot_req,fat_req,carb_req])])
    # Sort full df by distance to initial proportions
useful_df['prop_distance'] = np.sqrt((useful_df.prot_prop-proportions[0])**2+(useful_df.fat_prop - proportions[1])**2+(useful_df.carb_prop - proportions[2])**2)
    #temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)-1),:])
useful_df = useful_df.sort_values(by=['prop_distance'])
plan_df = pd.DataFrame([useful_df.iloc[0,:]])
useful_df = useful_df.drop(useful_df.index[[0]])
delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(plan_df['protein_g']),sum(plan_df['fat_g']),sum(plan_df['carb_g'])])
j = 0
while sum((abs(delta)<np.array([0.05*prot_req,0.05*fat_req,0.05*carb_req])))!=3:
    if sum(delta<0)==3:
        plan_df = plan_df.drop(plan_df.index[[randint(0,len(plan_df)-1)]])
    if j <= 4:
        plan_df, delta, proportions = add_sorted_item(useful_df[useful_df['rand_group']==j], plan_df, delta, proportions)
    else:
        plan_df, delta, proportions = add_sorted_item(useful_df, plan_df, delta, proportions)
    j+=1


plan_df.to_csv('plan_df_With_basic_bunches.csv', index=False)