import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import math
import time

# Global base_url variable
base_url = 'https://www.fatsecret.com'

glob_iter = 0 


def try_url(url):
    while True:
        try:
            page = requests.get(url)
            break
        except:
            time.sleep(30)
    ctr=0
    while(page.status_code!=200):
        if ctr>10&ctr<200:
            time.sleep(45)
        elif ctr>=200:
            break
        time.sleep(30)
        page = requests.get(url)
        ctr+=1 
    return page

def scrape_nutrients(prod_url):
    prod_page = try_url(prod_url)
    prod_soup = BeautifulSoup(prod_page.text, 'html.parser')
    fact_panel = prod_soup.find('div', attrs={'class':'nutpanel'})
    rows = fact_panel.findAll('tr')
    # Getting serving size
    for row in rows:
	    if row.text.strip().find('Serving Size:') != -1:
	        serving_size = row.text.strip().replace('Serving Size:', u'').strip()
	        serving_size = serving_size.replace('\r',u'').strip()
	        serving_size = serving_size.replace('\n',u' ').strip()
	        serving_size = serving_size.replace('\t',u'').strip()
	    elif row.text.strip().find('Calories') != -1:
	        calories = row.find('td').text.strip()
	        cal_label = row.find('b').text.strip()
	        cal_fat_label = row.find('div').text.strip()
	        calories = calories.replace(cal_fat_label, u'')
	        calories = calories.replace(cal_label, u'').strip()
	    elif row.text.strip().find('Total Fat') != -1:
	        fat = row.find('td').text.strip()
	        fat_label = row.find('td').find('b').text.strip()
	        fat = fat.replace(fat_label, u'').strip()
	    elif row.text.strip().find('Saturated Fat') != -1:
	        sat_fat = row.find('td', attrs={'class':'borderTop label'}).text.strip()
	        sat_fat = sat_fat.replace('Saturated Fat', u'').strip()
	    elif row.text.strip().find('Cholesterol') != -1:
	        cholesterol = row.find('td').text.strip()
	        cholesterol_label = row.find('td').find('b').text.strip()
	        cholesterol = cholesterol.replace(cholesterol_label, u'').strip()
	    elif row.text.strip().find('Sodium') != -1:
	        sodium = row.find('td').text.strip()
	        sodium_label = row.find('td').find('b').text.strip()
	        sodium = sodium.replace(sodium_label, u'').strip()
	    elif row.text.strip().find('Total Carbohydrate') != -1:
	        carb = row.find('td').text.strip()
	        carb_label = row.find('td').find('b').text.strip()
	        carb = carb.replace(carb_label, u'').strip()
	    elif row.text.strip().find('Dietary Fiber') != -1:
	        fiber = row.find('td', attrs={'class':'borderTop label'}).text.strip()
	        fiber = fiber.replace('Dietary Fiber', u'').strip()
	    elif row.text.strip().find('Sugars') != -1:
	        sugar = row.find('td', attrs={'class':'borderTop label'}).text.strip()
	        sugar = sugar.replace('Sugars', u'').strip()
	    elif row.text.strip().find('Protein') != -1:
	        protein = row.find('td').text.strip()
	        protein = protein.replace('Protein', u'').strip()
	    elif row.text.strip().find('Vitamin A') != -1:
	        vit_rows = row.findAll('td', attrs={'width':'50%'})
	        vit_a = vit_rows[0].text.strip().replace('Vitamin A',u'').strip()
	        vit_c = vit_rows[1].text.strip().replace('Vitamin C', u'').strip()
	    elif row.text.strip().find('Calcium') != -1:
	        calc_iron_rows = row.findAll('td', attrs={'width':'50%'})
	        calcium = calc_iron_rows[0].text.strip().replace('Calcium',u'').strip()
	        iron = calc_iron_rows[1].text.strip().replace('Iron', u'').strip()
    nut_df = pd.DataFrame([{"serving_size":serving_size, "calories":calories,"fat_g":fat.replace('g',u''),"saturated_fat_g":sat_fat.replace('g',u''),"cholesterol_mg":cholesterol.replace('mg',u''), "sodium_mg":sodium.replace('mg',u''),"carb_g":carb.replace('g',u''),"fiber_g":fiber.replace('g',u''),"sugar_g":sugar.replace('g',u''),"protein":protein.replace('g',u''),"vit_a_perc":vit_a.replace('%',u''),"vit_c_perc":vit_c.replace('%',u''),"calcium_perc":calcium.replace('%',u''),"iron_perc":iron.replace('%',u'')}])
    return nut_df

def parse_food_subgroup(url, group_name, sub_group_name):
    global glob_iter
    sub_cat_df = pd.DataFrame()
    sub_grp_pg = try_url(url)
    sub_grp_soup = BeautifulSoup(sub_grp_pg.text, 'html.parser')
    generic_box_sps = sub_grp_soup.findAll('table',attrs={'class':'generic nutrition'})
    for box in generic_box_sps:
        fd_label = np.nan
        foods = box.findAll('tr')
        for food in foods:
            try: 
                if 'food' in food['class']: # Dangerous, maybe should wrap in a try / except
                    food_name = food.find('a').text.strip()
                    food_link = base_url +  food.find('a')['href']
                    try:
                        nut_df = scrape_nutrients(food_link)
                        food_df = pd.DataFrame([{'food_group':group_name, 'food_sub_group':sub_group_name,'food':food_name, 'food_label':fd_label}])
                        row_df = pd.concat([food_df, nut_df], axis=1)
                        sub_cat_df = sub_cat_df.append([row_df],ignore_index=False) # Can re-order col names if it makes a difference
                    except:
                        print(food_name+' skipped')
                        pass
            except:
                if food.find('td', attrs={'class':'subtitle'}) != None:
                    fd_label =food.find('td', attrs={'class':'subtitle'}).find('h3').text.strip()
            

    if glob_iter == 0:
    	sub_cat_df.to_csv('fat_secret_groups_in_progress.csv', index=False)
    	glob_iter +=1
    else:
    	sub_cat_df.to_csv('fat_secret_groups_in_progress.csv', mode='a',index=False, header=False, index_label=0)
    return 'done'


def parse_food_group(url, group_name):
    food_pg = try_url(url)
    food_soup = BeautifulSoup(food_pg.text,'html.parser')
    food_sub_categories = food_soup.find('div', attrs={'class':'secHolder'})
    food_sub_subcategory_names = food_sub_categories.findAll('h2')
    for name in food_sub_subcategory_names:
        sub_cat_name = name.text.strip()
        sub_cat_link =  base_url+name.find('a')['href']
        parse_food_subgroup(sub_cat_link, group_name, sub_cat_name)
    return print(group_name + ' done parsing')

def parse_all_food_groups():
    start_url = 'https://www.fatsecret.com/calories-nutrition/group/beans-and-legumes'
    start_pg = try_url(start_url)
    start_soup = BeautifulSoup(start_pg.text, 'html.parser')
    grps_list_box = start_soup.find('div',attrs={'class':'linkHolder'}).find('table',attrs={'class':'common'})
    group_soup = grps_list_box.findAll('tr')
    for group in group_soup:
        group_name = group.find('a').text.strip()
        group_url = base_url + group.find('a')['href']
        parse_food_group(group_url, group_name)
    return print('finished food group parsing')

parse_all_food_groups()