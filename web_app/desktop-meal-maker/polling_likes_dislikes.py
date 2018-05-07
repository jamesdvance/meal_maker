def poll_raw_ingred():
    import warnings
    warnings.filterwarnings('ignore')
    import pandas as pd 
    from fuzzywuzzy import fuzz

    nut_sm = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_2018_3_15_processed_comma.csv', encoding='ISO-8859-1')
    raw_df = nut_sm[nut_sm.food_type_grp=='raw ingredient']
    raw_ingred = input("Tell me a raw ingredient you don't like: ")
    raw_df['ratios'] = raw_df['food_description'].map(lambda x: fuzz.ratio(x, raw_ingred))
    raw_df = raw_df.sort(['ratios'], ascending=False)

    raw_list = raw_df['food_description'].iloc[0:5]

    for item in raw_list:
        print(item)
        ans = int(input("Is this the food you were looking for: "+item+" ? (1/0)"))
        if ans == 1:
            return item
        else:
            pass
    
    print("Sorry, not found")
    return None

def poll_include():
    import warnings
    warnings.filterwarnings('ignore')
    import pandas as pd 
    from fuzzywuzzy import fuzz

    nut_sm = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_2018_3_15_processed_comma.csv', encoding='ISO-8859-1')
    fd_types = nut_sm['food_type_grp'].unique()
    fd_type = input("What type of food would you like to add? [raw ingredient, grocery, recipe, restaurant]?")
    while fd_type not in fd_types:
        fd_type= input("Sorry, that didn't match my options. What type of food would you like to add? [raw ingredient, grocery, recipe, restaurant]")
    
    raw_df = nut_sm[nut_sm.food_type_grp==fd_type]
    raw_ingred = input("Tell me a raw ingredient you want to eat this week: ")
    raw_df['ratios'] = raw_df['food_description'].map(lambda x: fuzz.ratio(x, raw_ingred))
    raw_df = raw_df.sort(['ratios'], ascending=False)

    raw_list = raw_df['food_description'].iloc[0:5]

    for item in raw_list:
        print(item)
        ans = int(input("Is this the food you were looking for: "+item+" ? (1/0)"))
        if ans == 1:
            return item
        else:
            pass
    
    print("Sorry, not found")
    return None

def poll_restaurants_nearbye():
    from googleplaces import GooglePlaces, types, lang
    import pandas as pd
    import requests
    import time
    # Api Keys
    api_keys = pd.read_csv("C:/Users/J/api_keys.csv")
    google_geo_api_key = api_keys['key_value'][api_keys.key_name=='google_places_api_key'].item()
    google_places_api_key = api_keys['key_value'][api_keys.key_name=='google_geo_api_key'].item()
    # Getting search criteria
    add = input("What is your full address (exlude apt)? ")
    add_f = add.replace(' ','+')
    lat_long_info = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+add_f+'&key='+google_geo_api_key)
    results = lat_long_info.json()['results']
    lat, lon = results[0]['geometry']['location']['lat'], results[0]['geometry']['location']['lng']
    google_places = GooglePlaces(google_places_api_key)
    result = google_places.nearby_search(
        pagetoken = None,
        location = add,
        lat_lng = {'lat':lat,'lng':lon},
        radius = 100,
        keyword = 'restaurant',
        rankby = 'distance',
        type=['restaurant']
    )
    rests = list(map(lambda x: x.name, result.places))
    while result.has_next_page_token:
        time.sleep(10)
        result = google_places.nearby_search(pagetoken=result.next_page_token,lat_lng = {'lat':lat,'lng':lon},)
        rests2 = list(map(lambda x: x.name, result.places))
    # Match with restaurants inside dataset - but then will have to 
    rests = rests + rests2
    kept_rests = process_liked_restaurants(rests)

   # Polling on likes / dislikes this week
    incl_rests = []
    for place in kept_rests:
        ans = int(input("Would you like to eat at "+place+" this week? (1/0)"))
        if ans == 1:
            incl_rests.append(place)
        else:
            pass

    return incl_rests
def process_liked_restaurants(near_me):
    import pandas as pd
    from fuzzywuzzy import fuzz
    from titlecase import titlecase

    df = pd.read_csv('C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_2018_3_15_processed_comma.csv', delimiter = ',',encoding='ISO-8859-1')
    all_restaurants = df.brand[df['food_type_grp']=='restaurant'].unique()
    

    my_rests = []
    for i in range(len(near_me)):
        near_me[i]= titlecase(near_me[i])
        rest = near_me[i]
        if rest in all_restaurants:
            my_rests.append(rest)

    remaining = set(near_me) - set(my_rests)

    if len(remaining)==0:
        return set(my_rests)
    else:
        for rem in remaining:
            for choice in all_restaurants:
                if fuzz.token_set_ratio(rem, choice)> 85: # dangerous threshold
                    my_rests.append(choice)
        return set(my_rests)



