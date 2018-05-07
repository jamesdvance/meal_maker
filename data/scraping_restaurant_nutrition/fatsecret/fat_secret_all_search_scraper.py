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

def parse_food_page(url, food_type):
    product_list_pg = try_url(url)
    product_list_soup = BeautifulSoup(product_list_pg.text, 'html.parser')
    results_sec = product_list_soup.find('table', attrs={'class':'generic searchResult'})
    if results_sec == None:
        rows = product_list_soup.findAll('tr')
    else:
        rows = results_sec.findAll('tr')
    full_page_df = pd.DataFrame()
    for row in rows:
        text_line = row.find('td',attrs={'class':'borderBottom'})
        food = text_line.find('a',attrs={'class':'prominent'}).text.strip()
        food_link = base_url+text_line.find('a',attrs={'class':'prominent'})['href']
        food_df = pd.DataFrame([{'food':food, 'brand':'all', 'food_type':food_type}])
        try:
            nut_df = scrape_nutrients(food_link)
            full_food_df = pd.concat([food_df, nut_df],axis=1)
            full_page_df = full_page_df.append([full_food_df], ignore_index=False)
        except: 
            print('skipped')
            pass
    return full_page_df

def parse_food_pages(url,food_type):
    global glob_iter
    food_pages_url = try_url(url)
    food_pages_soup = BeautifulSoup(food_pages_url.text, 'html.parser')
    search_summary = food_pages_soup.find('div',attrs={'class':'searchResultSummary'})
    if search_summary != None:
        try:
            txt = search_summary.text.strip()
        except:
            return 'done'
        total_products = txt[(txt.find('of')+2):txt.find('for')].strip()
        total_pages = math.ceil(int(total_products)/10)
        #food_df = pd.DataFrame()
        for i in range(16826):
            page_url = url+'&pg='+str(i)
            page_df = parse_food_page(page_url,food_type)
            #food_df = food_df.append(page_df)
            if glob_iter == 0:
                page_df.to_csv('fat_secret_all_search_progress.csv', index=False)
            else:
                page_df.to_csv('fat_secret_all_search_progress.csv', mode='a',index=False, header=False, index_label=0)
            glob_iter +=1
    return 'done' 


parse_food_pages('https://www.fatsecret.com/calories-nutrition/search?q=all','all')