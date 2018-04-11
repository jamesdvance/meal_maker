def poll_raw_ingred():
    import warnings
    warnings.filterwarnings('ignore')
    import pandas as pd 
    from fuzzywuzzy import fuzz

    nut_sm = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_2018_3_15_processed_comma.csv', encoding='ISO-8859-1')
    raw_df = nut_sm[nut_sm.food_type_grp=='raw ingredient']
    raw_ingred = input("Tell me a raw ingredient you don't like: ")
    raw_df['ratios'] = raw_df['food_desc'].map(lambda x: fuzz.ratio(x, raw_ingred))
    raw_df = raw_df.sort(['ratios'], ascending=False)

    raw_list = raw_df.iloc[0:5]

    no=True
    for item in raw_list:
    	while no:
	        no = (intinput("Is this the food you were looking for: "+item+" ? (1/0)"))
	        if no == 0:
	            no = True
	        else:
	            no = False
	            ingred = item
    if no:
        print("Sorry, not found")
        return None
    else:
        return ingred

