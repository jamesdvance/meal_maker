import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import math
import time



base_url = 'https://www.fatsecret.com'

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

def scrape_recipe(url):
    recipe_pg = try_url(url)
    recipe_soup = BeautifulSoup(recipe_pg.text, 'html.parser')
    # Yield
    if recipe_soup.find('div', attrs={'class':'yield'}) != None:
        recipe_yield = recipe_soup.find('div', attrs={'class':'yield'}).text.strip()
        recipe_yield_flt = float(recipe_yield.replace('serving',u'').strip().replace('s',u'').strip())
    else:
    	recipe_yield = np.nan
    # Prep Time
    if recipe_soup.find('div', attrs={'class':'prepTime'}) != None:
    	prep_time = recipe_soup.find('div', attrs={'class':'prepTime'}).text.strip()
    else:
    	prep_time = np.nan
    if recipe_soup.find('div', attrs={'id':'mealtypes'}) != None:
        meal_type_soup = recipe_soup.find('div', attrs={'id':'mealtypes'})
        tags = meal_type_soup.findAll('div', attrs={'class':'tag'})
        tag_arr = '{'
        for tag in tags:
            tag_arr = tag_arr + tag.text.strip()+'| '
        tag_arr = tag_arr[0:(len(tag_arr)-2)]
        meal_type = tag_arr + '}'
    else:
    	meal_type = np.nan
    # Meal Type
    # Ingredients
    ingred_list = recipe_soup.find('ul',attrs={'class':'plain ingredients'}).findAll('li',attrs={'class':'ingredient'})
    food_arr = '{'
    amount_arr = '{'
    for ingred in ingred_list:
        food_arr = food_arr + ingred.find('a')['title'].strip() + ', '
        amount_arr = amount_arr  + ingred.text.strip()  + '| '
    food_arr=food_arr[0:(len(food_arr)-2)]
    amount_arr=amount_arr[0:(len(amount_arr)-2)]
    food_arr = food_arr + '}'
    amount_arr = amount_arr+'}'
    ingred_arr = '{' + food_arr +', '+amount_arr+'}'
    # Instructions
    directions_list = recipe_soup.find('ol',attrs={'class':'noind instructions'}).findAll('li',attrs={'class':'instruction'})
    instructions_arr = '{'
    for instr in directions_list:
        instructions_arr = instructions_arr + instr.text.strip()+'| '
    instructions_arr=instructions_arr[0:(len(instructions_arr)-2)]
    instructions_arr = instructions_arr + '}'
    recipe_facts_df = pd.DataFrame([{'ingredient_list':food_arr, 'quantities_list':amount_arr, 'full_ingred_list':ingred_arr,'instructions':instructions_arr, 'yield':recipe_yield_flt,'meal_type':meal_type}])
    nut_df = scrape_nutrients(url)
    recipe_df = pd.concat([recipe_facts_df, nut_df],axis=1)
    return recipe_df

def scrape_recipes(url, start):
    recipe_list_pg = try_url(url)
    recipe_list_soup = BeautifulSoup(recipe_list_pg.text, 'html.parser')
    results_table = recipe_list_soup.find('table',attrs={'class':'listtable searchResult', 'width':'100%'})
    results_rows = results_table.findAll('tr', attrs={'class':'listrow'})
    recipe_full_df = pd.DataFrame()
    for row in results_rows:
    # taking a very simple approach
        recipe_name = row.find('b').text.strip()
        if row.find('div',attrs={'class':'topicsummary'}) != None:
            recipe_desc = row.find('div',attrs={'class':'topicsummary'}).text.strip()
        else: 
            recipe_desc = np.nan
        recipe_link = base_url + row.find('b').find('a')['href']
        recipe_name_df = pd.DataFrame([{'recipe_name':recipe_name,'recipe_desc':recipe_desc}])
        recipe_df = scrape_recipe(recipe_link)
        recipe_lines_df = pd.concat([recipe_name_df, recipe_df], axis=1)
        recipe_full_df = recipe_full_df.append([recipe_lines_df], ignore_index=False)
    if start:
        recipe_full_df.to_csv("fat_secret_recipe_in_progress.csv",index=False)
    else:
    	recipe_full_df.to_csv('fat_secret_recipe_in_progress.csv', mode='a',index=False, header=False, index_label=0)
    return 'scraped'

def scrape_all_recipes():
    start_url = 'https://www.fatsecret.com/Default.aspx?pa=rs'
    start_pg = try_url(start_url)
    start_soup = BeautifulSoup(start_pg.text,'html.parser')
    link_section = start_soup.find('div',attrs={'class':'searchResultsPaging'})
    recipe_pages = link_section.findAll('a')
    links = []
    for page in recipe_pages:
        if base_url + page['href'] != start_url:
            links.append(base_url + page['href'])
        else:
            pass
    links = links[0:(len(links)-1)]
    
    i = 0
    for link in links:
    	if i >0:
    	    scrape_recipes(link, False)
    	else:
    		scrape_recipes(link, True)
    	i+=1
    return print('scraping recipes finished')

#scrape_recipes('https://www.fatsecret.com/Default.aspx?pa=rs',True)
scrape_all_recipes()