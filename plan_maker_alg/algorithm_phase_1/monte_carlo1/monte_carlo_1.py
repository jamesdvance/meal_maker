import pandas as pd
import numpy as np
from random import randint


full_df = pd.read_csv("branded_foods_in_progress.csv")
alpha_df = full_df[['ndb_no','desc_only','kilocalories', 'protein_g','fat_g','carb_g','unit_per_item']]
useful_df = alpha_df[alpha_df['kilocalories']>0]
useful_df.protein_g[useful_df['protein_g'].isnull()] = 0
useful_df.fat_g[useful_df['fat_g'].isnull()] = 0
useful_df.carb_g[useful_df['carb_g'].isnull()] = 0
useful_df.isnull().sum()
useful_df.protein_g = useful_df.protein_g.astype(int)
useful_df.fat_g = useful_df.fat_g.astype(int)
useful_df.carb_g = useful_df.carb_g.astype(int)

def find_a_plan(prot_req, fat_req, carb_req):# First Iter
    temp_df = pd.DataFrame()
    plan_df = pd.DataFrame()
    plan_id = 0
    # Insert Logic Here
    # If at least one of the delta values is over 50% of final target
    it=0
    drop_it = 0
    for i in range(30000):
        temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)-1),:])
        delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(temp_df['protein_g']),sum(temp_df['fat_g']),sum(temp_df['carb_g'])])

        while sum((delta<np.array([0,0,0])))>0:
            temp_df = temp_df.drop(temp_df.index[[randint(0,len(temp_df)-1)]])
            delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(temp_df['protein_g']),sum(temp_df['fat_g']),sum(temp_df['carb_g'])])
            drop_it+=1
            print(drop_it)
        print(str(i)+ ' iterations')
        print(str(len(temp_df))+' items considered')
        print(delta)
        if sum((delta<np.array([prot_req*.5,fat_req*.5,carb_req*.5])))>0:
            match_df = useful_df[(useful_df['protein_g']==delta[0])& (useful_df['fat_g']==delta[1]) & (useful_df['fat_g']==delta[2])]
            if len(match_df)==0:
                # Add a random item
                it+=1
                # Drop a random item
                if it%2 ==0:
                    temp_df = temp_df.drop(temp_df.index[[randint(0,len(temp_df)-1)]])
                delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(temp_df['protein_g']),sum(temp_df['fat_g']),sum(temp_df['carb_g'])])
            else:
                for j in range(len(match_df)):
                    plan_id+=1
                    temp_df = temp_df.append(match_df.iloc[j,:])
                    plan_df = plan_df.append([{'ndb_no':temp_df['ndb_no'], 'plan_id':[plan_id]*len(temp_df)}])
                return pd.DataFrame([{'prot_req':prot_req,
                                      'fat_req':fat_req,
                                      'carb_req':carb_req,
                                      'num_items':len(temp_df),
                                      'num_matches':len(match_df),
                                      'mac_proportions':sum([abs(prot_req-fat_req),abs(fat_req-carb_req),abs(prot_req-carb_req)]),
                                      'iterations':i,
                                      'prot_delta': delta[0],
                                      'fat_delta': delta[1],
                                      'carb_delta': delta[2]
                                     }])
    return pd.DataFrame([{'prot_req':prot_req,
                                      'fat_req':fat_req,
                                      'carb_req':carb_req,
                                      'num_items':len(temp_df),
                                      'num_matches':len(match_df),
                                      'mac_proportions':sum([abs(prot_req-fat_req),abs(fat_req-carb_req),abs(prot_req-carb_req)]),
                                      'iterations':i,
                                      'prot_delta': delta[0],
                                      'fat_delta': delta[1],
                                      'carb_delta': delta[2]
                                     }])

def monte_carlo_maker(iterations):
    mc_df = pd.DataFrame()
    for i in range(iterations):
        req1 = randint(20,220)
        req2 = randint(20,220)
        req3 = randint(20,220)
        result = find_a_plan(req1 , req2, req3)
        mc_df.append(result, ignore_index=True)
    return mc_df


test = monte_carlo_maker(10000)

test.to_csv('test.csv')