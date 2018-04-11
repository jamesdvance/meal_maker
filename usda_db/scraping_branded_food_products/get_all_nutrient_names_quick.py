from bs4 import BeautifulSoup
import requests 
import pandas as pd


start_url = "https://ndb.nal.usda.gov/ndb/nutrients/index?fg=&nutrient1=221&nutrient2=&nutrient3=&subset=0&sort=f&totCount=0&offset=0&measureby=m"

page = requests.get(start_url)

soup_obj = BeautifulSoup(page.text, 'html.parser')

nut_obj = soup_obj.find('select', attrs={'id':'nutrient2','name':'nutrient2'})

nut_options = nut_obj.findAll('option')

option_vec = []
for option in nut_options:
	option_vec.append(option.text.strip())

option_df = pd.DataFrame(option_vec)

option_df.to_csv("full_nut_options_list.csv")