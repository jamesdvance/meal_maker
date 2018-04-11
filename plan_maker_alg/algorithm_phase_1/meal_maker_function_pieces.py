





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

def add_non_sorted_item(useful_df, plan_df, delta, proportions): # When would I ever need this?
	return plan_df, delta, proportions