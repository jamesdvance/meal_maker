# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 08:54:45 2018

@author: J
"""
# Qdoba Burrito - Cal, Carb, Fat, Protein, Fiber
link1 = 'http://www.dietfacts.com/html/nutrition-facts/qdoba-mexican-grill-chicken-burrito-with-rice-and-cheese-mild-no-beans-13-inch-flour-tortil9555.htm'


def parse_nut_info(nut_soup):
	# Getting the Right Soup
	nut_space = nut_soup.findAll('basefont')[1].findAll('tr')
	# Extracting Variables
	product_name = nut_soup.find('h1').text # Should be universal. Is NA otherwise
    
	serving_size = nut_space[0].find('td').findAll('nobr')[0].text + ' ' + nut_space[0].find('td').findAll('nobr')[1].text
	calories = nut_space[0].find('td').findAll('font')[3].text
	calories_from_fat = nut_space[0].find('td').findAll('nobr')[2].text
	total_fat = nut_space[0].find('td').findAll('font')[6].text+' '+nut_space[0].find('td').findAll('font')[7].text
	saturated_fat = nut_space[0].find('td').findAll('font')[9].text
	cholesterol = nut_space[0].find('td').findAll('font')[11].text
	sodium = nut_space[0].find('td').findAll('font')[13].text
	total_carb = nut_space[0].find('td').findAll('font')[15].text
	total_fiber = nut_space[0].find('td').findAll('font')[17].text
	total_protein = nut_space[0].find('td').findAll('font')[19].text
	nutrients_list = [serving_size,calories,calories_from_fat, total_fat, saturated_fat, cholesterol, sodium,total_carb, total_fiber,total_protein]
	nutrient_col = []
	value_col =[]
	for item in nutrients_list:
	    new_item = item.replace('\xa0',u' ').strip()
	    if len(re.split(u'  ', new_item))==2:
	        nutrient_col.append(re.split(u'  ', new_item)[0])
	        value_col.append(re.split(u'  ', new_item)[1])
	    else:
	        nutrient_col.append(re.split(u' ', new_item)[0])
	        value_col.append(re.split(u' ', new_item)[1])
	nutrient_df = pd.DataFrame([value_col],columns=nutrient_col)
	item_name_df = pd.DataFrame([{'Item Name':product_name}])
	nutrient_df = pd.concat([item_name_df, nutrient_df], axis=1)
	return nutrient_df