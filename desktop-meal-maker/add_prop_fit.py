def add_prop_fit(useful_df, plan_df, proportions, cal_delta):
    #
    eval_df = useful_df[['food_key','calories', 'prot_prop','carb_prop','fat_prop']]
    #
    eval_df['cal_distance'] =  np.sqrt((eval_df.calories - cal_delta)**2)
    # Doesn't have to be quantile - can just be some percentage close to zero
    eval_df['macro_distance'] = np.sqrt((eval_df.prot_prop-proportions[0])**2+(eval_df.fat_prop - proportions[1])**2+(eval_df.carb_prop - proportions[2])**2) 
    #
    # Could bin the distances in groups of ntile(20), and then pull the best proportions from those groups
    # Would be nice if it had some sort of random process at the start that got narrower and narrower towards reqs.
    eval_df['cal_ntile'] = pd.qcut(eval_df.cal_distance, q=30)
    eval_df = eval_df.sort_values(by=['macro_distance'])
    # Could we select the top n % by a random distribution favoring the top, 
# Append closest distance
    plan_df = plan_df.append([eval_df.iloc[0,:]],ignore_index=True)
    cal_delta = sum(plan_df.calories) - cal_delta
    prot = sum(plan_df.protein_g)
    fat = sum(plan_df.fat_g)
    carb = sum(plan_df.carb_g)
    
    proportions = np.array([prot/(prot+fat+carb),fat/(prot+fat+carb),carb/(prot+fat+carb)])

    return plan_df, cal_delta, proportions
    