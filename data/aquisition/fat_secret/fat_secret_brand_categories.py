import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import math
import time

# Global base_url variable
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


def parse_letters(url,char,t):
    start_letter_pg = try_url(url)
    start_letter_soup = BeautifulSoup(start_letter_pg.text,'html.parser')
    n_letter_pages = start_letter_soup.find('div', attrs={'class':'searchResultSummary'}).text.strip()
    total_entries = n_letter_pages[(n_letter_pages.find('of')+2):len(n_letter_pages)].strip()
    total_pages = math.ceil(int(total_entries)/20)
    food_types = {1:'grocery',2:'restaurant',3:'super_market',4:'other'}
    food_type = food_types[t]
    brand_list = []
    for i in range(total_pages):
        page_url = base_url+'/Default.aspx?pa=brands&pg='+str(i)+'&f='+char.lower()+'&t='+str(t)
        brand_pages_pg = try_url(url)
        brand_pages_soup = BeautifulSoup(brand_pages_pg.text, 'html.parser')
        brand_sec = brand_pages_soup.find('div', attrs={'class':'leftCellContent'})
        brands = brand_sec.findAll('h2')
        for brand in brands:
            brand_list.append(brand.text.strip())
    return brand_list

def parse_all_chars():
    chars_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','*']
    grocery_list =[]
    restaurant_list = []
    for t in range(2,4):
        for char in chars_list:
            start_url = base_url+'/Default.aspx?pa=brands&pg=0&f='+char.lower()+'&t='+str(t)
            iter_list = parse_letters(start_url,char,t)
            if t == 2:
                restaurant_list = restaurant_list + iter_list
            else:
                grocery_list = grocery_list + iter_list
    restaurant_df = pd.DataFrame(restaurant_list)
    restaurant_df.to_csv("restaurant_brands.csv", index=False)
    grocery_df = pd.DataFrame(grocery_list)
    grocery_df.to_csv("grocery_brands.csv", index=False)
    return 'finished'

parse_all_chars()