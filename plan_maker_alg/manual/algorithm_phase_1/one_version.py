# First Iter
temp_df = pd.DataFrame()
plan_df = pd.DataFrame()
plan_id = 0
# Insert Logic Here
temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)),:])
delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(temp_df['protein_g']),sum(temp_df['fat_g']),sum(temp_df['carb_g'])])
# If at least one of the delta values is over 50% of final target
it=0
while True:
    temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)),:])
    if sum((delta>np.array([prot_req*.5,fat_req*.5,carb_req*.5])))>0:
        match_df = useful_df[useful_df[['protein_g']]==delta[0]]
        if len(match_df)==0:
            # Add a random item
            it+=1
            temp_df = temp_df.append(useful_df.iloc[randint(0,len(useful_df)),:])
            # Drop a random item
            if it%2 ==0:
                temp_df = temp_df.drop[temp_df.index(randint(0,len(temp_df)))]
            delta = np.array([prot_req,fat_req,carb_req])-np.array([sum(temp_df['protein_g']),sum(temp_df['fat_g']),sum(temp_df['carb_g'])])
        else:
            for i in range(len(match_df)):
                plan_id+=1
                temp_df = temp_df.append(match_df.iloc[i,:])
                plan_df = plan_df.append([{'ndb_no':temp_df['ndb_no'], 'plan_id':[plan_id]*len(temp_df)}])
            break