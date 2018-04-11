from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np
import time
import re
import sys
sys.path.append('C:/Users/J/Desktop/Git_Repositories/scraping_restaurant_nutrition')
from nutrient_finder_functions_w_nan import *

def parse_nut_info(nut_soup):
    # Getting the Right Soup
    # without using classes
    nut_space = nut_soup.findAll('basefont')[1].findAll('tr')

    # Item name
    item_name = nut_soup.find('h1').text
    try:
        item_desc = nut_soup.findAll('tr')[3].findAll('h2')[1].text.strip()
    except:
        item_desc = 'not found'
    brand_name = get_brand_name(nut_soup)
    # Extracting Variables
    serving_size = get_serving_size(nut_space[0])
    calories = get_calories(nut_space[0])
    total_fat = get_total_fat(nut_space[0])
    sat_fat = get_saturated_fat(nut_space[0])
    trans_fat = get_trans_fat(nut_space[0])
    cholesterol = get_cholesterol(nut_space[0])
    sodium = get_sodium(nut_space[0])
    potassium = get_potassium(nut_space[0])
    carb = get_total_carb(nut_space[0])
    fiber = get_dietary_fiber(nut_space[0])
    sugars = get_sugars(nut_space[0])
    protein = get_protein(nut_space[0])
    vit_a = get_vitamin_a(nut_soup)
    vit_c = get_vitamin_c(nut_soup)
    calcium = get_calcium(nut_soup)
    iron = get_iron(nut_soup)
    
    nutrient_df = pd.DataFrame([{
            'brand_name':brand_name,
            'item_name':item_name,
            'item_desc':item_desc,
            'serving_size':serving_size,
            'calories':calories,
            'fat_g':total_fat,
            'saturated_fat_g':sat_fat,
            'trans_fat_g':trans_fat,
            'cholesterol_mg':cholesterol,
            'sodium_mg':sodium,
            'potassium_mg':potassium,
            'carb_g':carb,
            'fiber_g':fiber,
            'sugar_g':sugars,
            'protein_g':protein,
            'vit_a_perc':vit_a,
            'vit_c_perc':vit_c,
            'calcium_perc':calcium,
            'iron_perc':iron
            }])
    return nutrient_df

def parse_food_item_info(url):
    food_df = pd.DataFrame()
    # Getting the right soup
    while True:
        try:
            rest_page = requests.get(url)
            break
        except:
            time.sleep(20)
    rest_soup = BeautifulSoup(rest_page.text, 'html.parser')
    base_url = 'http://www.dietfacts.com/'
    # Need to check if this is just a plain recipe page
    # Finding all the links
    a_links = rest_soup.findAll('table')[2].findAll('a')
    rest_links = []
    rest_food_names = []
    for a in a_links:
        try:
            if re.search('html/nutrition-facts',a['href'])!=None:
                if a.find('b') != -1:
                    food_url = base_url+a['href']
                    while True:
                        try:
                            nut_page = requests.get(food_url)
                            break
                        except:
                            time.sleep(20)
                    nut_soup = BeautifulSoup(nut_page.text, 'html.parser')
                    nut_df = parse_nut_info(nut_soup)
                    food_df = food_df.append(nut_df)
        except:
            pass
    food_df = food_df
    return food_df
def parse_brand_pages(url):
    # Getting the right soup
    while True:
        try:
            rest_page = requests.get(url)
            break
        except:
            time.sleep(20)
    rest_soup = BeautifulSoup(rest_page.text, 'html.parser')

    if re.search(r'itemid=', url) != None:
        food_df = parse_nut_info(rest_soup)
        return food_df

    food_df = parse_food_item_info(url)

    n_pages = n_items(rest_soup)

    if (n_pages !='not found') and int(n_pages)>1:
        for i in range(2, int(n_pages)+1):
            new_url = url+'&page='+str(i)
            new_df = parse_food_item_info(new_url)
            food_df = food_df.append(new_df,ignore_index=True)
    food_df = food_df.drop_duplicates()
    return food_df

#Needs to label these as from 'restaurants'
# Then can seperately scrape by brand, and anti_join with restaurant data
# But still have a common field called 'brand'. And then another 'Category': restaurant/brand
def parse_all_restaurants(start_url):
    # Getting the right soup
    #full_df = pd.DataFrame()
    ff_start = requests.get(start_url)
    ff_soup = BeautifulSoup(ff_start.text,'html.parser')
    ff_plain = ff_soup.findAll('a',attrs={'class':'plain'})
    # Finding all restaurants
    ff_links = []
    ff_restaurants = []
    for line in ff_plain:
        if line.find('strike') == None:
            ff_links.append(line['href'])
            ff_restaurants.append(line.text)
    # Formatting links to be useable
    base_url = 'http://www.dietfacts.com/'
    ff_links_full = [base_url+link for link in ff_links]
    #for i in range(0,5): # for testing - ignoring the bbq sauce
    for i in range(len(ff_links_full)-1):
        if zero_finder(ff_links_full[i]):
            page_df = parse_brand_pages(ff_links_full[i])
            page_df['brand_label'] = ff_restaurants[i]
            page_df['category'] = 'restaurant'
            if i> 0:
                page_df.to_csv('restaurant_foods_in_progress.csv', mode='a',index=False, header=False, index_label=0)
            else:
                page_df.to_csv('restaurant_foods_in_progress.csv', index=False)
            print('Page '+str(i)+' scraped')
        else:
            pass
        #full_df = full_df.append(rest_df, ignore_index=True)
    #full_df['category'] = 'restaurant'
    return 'done'

# Test a bunch of different pages and look at what gets included and what doesn't.

big_df = parse_all_restaurants('http://www.dietfacts.com/fastfood.asp')
#big_df.to_csv("big_df_results.csv",index=False)