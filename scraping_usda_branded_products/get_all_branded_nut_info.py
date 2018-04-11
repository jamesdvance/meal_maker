from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np
import time
import re

# Programs: scrape_foods_page, scrape_nutrient_page, parse_pages
column_name_lookup = {
"Water":"water", 
"Energy":"kilocalories", 
"Protein":"protein_g", 
"Total lipid (fat)":"fat_g", 
"Ash":"ash_g", 
"Carbohydrate, by difference":"carb_g", 
"Fiber, total dietary":"fiber_g", 
"Sugars, total":"sugar_g", 
"Sucrose":"sucrose_g", 
"Glucose (dextrose)":"glucose_g", 
"Fructose":"fructose_g", 
"Lactose":"lactose_g", 
"Maltose":"maltose_g", 
"Galactose":"galactose_g", 
"Starch":"starch_g", 
"Calcium, Ca":"calcium_mg", 
"Iron, Fe":"iron_mg", 
"Magnesium, Mg":"magnesium_mg", 
"Phosphorus, P":"phosphorus_mg", 
"Potassium, K":"potassium_mg", 
"Sodium, Na":"sodium_mg", 
"Zinc, Zn":"zinc_mg", 
"Copper, Cu":"copper_mg", 
"Manganese, Mn":"manganese_mg", 
"Selenium, Se":"selenium_mcg", 
"Fluoride, F":"flouride_mcg", 
"Vitamin C, total ascorbic acid":"vit_c_mg", 
"Thiamin":"thiamin_mg", 
"Riboflavin":"riboflavin_mg", 
"Niacin":"niacin_mg", 
"Pantothenic acid":"panto_acid_mg", 
"Vitamin B-6":"vit_b6_mg", 
"Folate, total":"folate_mcg", 
"Folic acid":"folic_acid_mcg", 
"Folate, food":"food_folate_mcg", 
"Folate, DFE":"folate_mcg_dfe", 
"Choline, total":"choline_mg", 
"Betaine":"betaine_mg", 
"Vitamin B-12":"vit_b12_mcg", 
"Vitamin B-12, added":"vit_b12_added_mcg", 
"Vitamin A, RAE":"vit_a_mcg_rae", 
"Retinol":"retinol_mcg", 
"Carotene, beta":"beta_carotene_mcg", 
"Carotene, alpha":"alpha_carotene_mcg", 
"Cryptoxanthin, beta":"beta_cryptoxanthin_mcg", 
"Vitamin A, IU":"vit_a_iu", 
"Lycopene":"lycopene_mcg", 
"Lutein + zeaxanthin":"lutein_zeazanthin_mcg", 
"Vitamin E (alpha-tocopherol)":"vit_e_mg", 
"Vitamin E, added":"", 
"Tocopherol, beta":"beta_tocopherol_mg", 
"Tocopherol, gamma":"gamma_tocopherol_mg", 
"Tocopherol, delta":"delta_tocopherol_mg", 
"Tocotrienol, alpha":"alpha_tocopherol_mg", 
"Tocotrienol, beta":"beta_tocotrienol_mg", 
"Tocotrienol, gamma":"gamma_tocotrienol_mg", 
"Tocotrienol, delta":"delta_tocotrienol_mg", 
"Vitamin D (D2 + D3)":"vit_d_mcg", 
"Vitamin D2 (ergocalciferol)":"vit_d2_mcg", 
"Vitamin D3 (cholecalciferol)":"vit_d3_mcg", 
"Vitamin D":"vit_d_ui", 
"Vitamin K (phylloquinone)":"vit_k_mcg", 
"Dihydrophylloquinone":"dihydrophylloquinone_mcg", 
"Menaquinone-4":"menaquinone_4_mcg", 
"Fatty acids, total saturated":"saturated_fatty_acid_g", 
"4:0":"ratio_4_0_g", 
"6:0":"ratio_6_0_g", 
"8:0":"ratio_8_0_g", 
"10:0":"ratio_10_0_g", 
"12:0":"ratio_12_0_g", 
"13:0":"ratio_13_0_g", 
"14:0":"ratio_14_0_g", 
"15:0":"ratio_15_0_g", 
"16:0":"ratio_16_0_g", 
"17:0":"ratio_17_0_g", 
"18:0":"ratio_18_0_g", 
"20:0":"ratio_20_0_g", 
"22:0":"ratio_22_0_g", 
"24:0":"ratio_24_0_g", 
"Fatty acids, total monounsaturated":"monosaturated_fatty_acid_g", 
"14:1":"ratio_14_1_g", 
"15:1":"ratio_15_1_g", 
"16:1 undifferentiated":"ratio_16_1_undif_g", 
"16:1 c":"ratio_16_1_c_g", 
"16:1 t":"ratio_16_1_t_g", 
"17:1":"ratio_17_1_g", 
"18:1 undifferentiated":"ratio_18_1_undif_g", 
"18:1 c":"ratio_18_1_c_g", 
"18:1 t":"ratio_18_1_t_g", 
"18:1-11 t (18:1t n-7)":"", 
"20:1":"", 
"22:1 undifferentiated":"", 
"22:1 c":"", 
"22:1 t":"", 
"24:1 c":"", 
"Fatty acids, total polyunsaturated":"polysaturated_fatty_acid_g", 
"18:2 undifferentiated":"ratio_18_2_undif_g", 
"18:2 n-6 c,c":"ratio_18_2_n_6_cc_g", 
"18:2 CLAs":"ratio_18_2_cla_g", 
"18:2 t,t":"ratio_18_2_t_t_g", 
"18:2 i":"ratio_18_2_i_g", 
"18:2 t not further defined":"ratio_18_2_not_def_g", 
"18:3 undifferentiated":"ratio_18_3_undif_g", 
"18:3 n-3 c,c,c (ALA)":"ratio_18_3_n3_ccc_g", 
"18:3 n-6 c,c,c":"ratio_18_3_n6_ccc_g", 
"18:3i":"ratio_18_3_i_g", 
"18:4":"ratio_18_4_g", 
"20:2 n-6 c,c":"ratio_20_2_n6_cc_g", 
"20:3 undifferentiated":"ratio_20_3_undif_g", 
"20:3 n-3":"ratio_20_3_n3_g", 
"20:3 n-6":"ratio_20_3_n6_g", 
"20:4 undifferentiated":"ratio_20_4_undif_g", 
"20:4 n-6":"ratio_20_4_n6_g", 
"20:5 n-3 (EPA)":"ratio_20_5_n3_epa_g", 
"21:5":"ratio_21_5_g", 
"22:4":"ratio_22_4_g", 
"22:5 n-3 (DPA)":"ratio_22_5_n3_dpa_g", 
"22:6 n-3 (DHA)":"ratio_22_6_n3_dha_g", 
"Fatty acids, total trans":"trans_fatty_acid_g", 
"Fatty acids, total trans-monoenoic":"trans_monoenoic_fatty_acid_g", 
"Fatty acids, total trans-polyenoic":"trans_polyenoic_fatty_acid_g", 
"Cholesterol":"cholesterol_mg", 
"Phytosterols":"phytosterols_mg", 
"Stigmasterol":"stigmasterol_mg", 
"Campesterol":"campesterol_mg", 
"Beta-sitosterol":"beta_sitosterol_mg", 
"Tryptophan":"tryptophan_g", 
"Threonine":"threonine_g", 
"Isoleucine":"isoleucine_g", 
"Leucine":"leucine_g", 
"Lysine":"lysine_g", 
"Methionine":"methionine_g", 
"Cystine":"cystine_g", 
"Phenylalanine":"phenylalanine_g", 
"Tyrosine":"tyrosine_g", 
"Valine":"valine_g", 
"Arginine":"arginine_g", 
"Histidine":"histidine_g", 
"Alanine":"alanine_g", 
"Aspartic acid":"aspartic_acid_g", 
"Glutamic acid":"glutamic_acid_g", 
"Glycine":"glycine_g", 
"Proline":"proline_g", 
"Serine":"serine_g", 
"Hydroxyproline":"hydroxyproline_g", 
"Alcohol, ethyl":"ethyl_alcohol_g", 
"Caffeine":"caffeine_mg", 
"Theobromine":"theobromine_mg", 
}

full_columns = ["ndb_no", 
"short_desc", 
"manufac_fd_grp", 
"ingredients_list", 
"unit_per_item", 
"water", 
"kilocalories", 
"protein_g", 
"fat_g", 
"ash_g", 
"carb_g", 
"fiber_g", 
"sugar_g", 
"calcium_mg", 
"iron_mg", 
"magnesium_mg", 
"phosphorus_mg", 
"potassium_mg", 
"sodium_mg", 
"zinc_mg", 
"copper_mg", 
"manganese_mg", 
"selenium_mcg", 
"vit_c_mg", 
"thiamin_mg", 
"riboflavin_mg", 
"niacin_mg", 
"panto_acid_mg", 
"vit_b6_mg", 
"folate_mcg", 
"folic_acid_mcg", 
"food_folate_mcg", 
"folate_mcg_dfe", 
"choline_mg", 
"vit_b12_mcg", 
"vit_a_iu", 
"vit_a_mcg_rae", 
"retinol_mcg", 
"alpha_carotene_mcg", 
"beta_carotene_mcg", 
"beta_cryptoxanthin_mcg", 
"lycopene_mcg", 
"lutein_zeazanthin_mcg", 
"vit_e_mg", 
"vit_d_mcg", 
"vit_d_ui", 
"vit_k_mcg", 
"saturated_fatty_acid_g", 
"monosaturated_fatty_acid_g", 
"polysaturated_fatty_acid_g", 
"cholesterol_mg", 
"gm_weight_1", 
"gm_weight_desc1", 
"gm_weight_2", 
"gm_weight_desc2", 
"refuse_pct", 
"kilojoules", 
"sucrose_g", 
"glucose_g", 
"fructose_g", 
"lactose_g", 
"maltose_g", 
"galactose_g", 
"starch_g", 
"flouride_mcg", 
"betaine_mg", 
"vit_b12_added_mcg", 
"vit_e_added_mg", 
"beta_tocopherol_mg", 
"gamma_tocopherol_mg", 
"delta_tocopherol_mg", 
"alpha_tocopherol_mg", 
"beta_tocotrienol_mg", 
"gamma_tocotrienol_mg", 
"delta_tocotrienol_mg", 
"vit_d2_mcg", 
"vit_d3_mcg", 
"dihydrophylloquinone_mcg", 
"menaquinone_4_mcg", 
"ratio_4_0_g", 
"ratio_6_0_g", 
"ratio_8_0_g", 
"ratio_10_0_g", 
"ratio_12_0_g", 
"ratio_13_0_g", 
"ratio_14_0_g", 
"ratio_15_0_g", 
"ratio_16_0_g", 
"ratio_17_0_g", 
"ratio_18_0_g", 
"ratio_20_0_g", 
"ratio_22_0_g", 
"ratio_24_0_g", 
"ratio_14_1_g", 
"ratio_15_1_g", 
"ratio_16_1_undif_g", 
"ratio_16_1_c_g", 
"ratio_16_1_t_g", 
"ratio_17_1_g", 
"ratio_18_1_undif_g", 
"ratio_18_1_c_g", 
"ratio_18_1_t_g", 
"ratio_18_2_undif_g", 
"ratio_18_2_n_6_cc_g", 
"ratio_18_2_cla_g", 
"ratio_18_2_t_t_g", 
"ratio_18_2_i_g", 
"ratio_18_2_not_def_g", 
"ratio_18_3_undif_g", 
"ratio_18_3_n3_ccc_g", 
"ratio_18_3_n6_ccc_g", 
"ratio_18_3_i_g", 
"ratio_18_4_g", 
"ratio_20_2_n6_cc_g", 
"ratio_20_3_undif_g", 
"ratio_20_3_n3_g", 
"ratio_20_3_n6_g", 
"ratio_20_4_undif_g", 
"ratio_20_4_n6_g", 
"ratio_20_5_n3_epa_g", 
"ratio_21_5_g", 
"ratio_22_4_g", 
"ratio_22_5_n3_dpa_g", 
"ratio_22_6_n3_dha_g", 
"trans_fatty_acid_g", 
"trans_monoenoic_fatty_acid_g", 
"trans_polyenoic_fatty_acid_g", 
"phytosterols_mg", 
"stigmasterol_mg", 
"campesterol_mg", 
"beta_sitosterol_mg", 
"tryptophan_g", 
"threonine_g", 
"isoleucine_g", 
"leucine_g", 
"lysine_g", 
"methionine_g", 
"cystine_g", 
"phenylalanine_g", 
"tyrosine_g", 
"valine_g", 
"arginine_g", 
"histidine_g", 
"alanine_g", 
"aspartic_acid_g", 
"glutamic_acid_g", 
"glycine_g", 
"proline_g", 
"serine_g", 
"hydroxyproline_g", 
"ethyl_alcohol_g", 
"caffeine_mg", 
"theobromine_mg"]

def parse_foods_page(page_url):
	# Page Dataframe Building Blocks
	page_df = pd.DataFrame(columns=full_columns)
	while True:
		try:
			page = requests.get(page_url)
			break
		except:
			time.sleep(20)
	main_soup = BeautifulSoup(page.text, 'html.parser')
	table_lines = main_soup.find('tbody').findAll('tr')
	base_url = 'https://ndb.nal.usda.gov'
	for line in table_lines:
		# Getting url
		cur_line = line.findAll('td')
		url_tail = cur_line[1].findAll('a')[0]['href']
		food_url = base_url + url_tail
		# Scraping Inner Page Values
		inner_pg_df = parse_nutrient_page(food_url)
		# Scraping Front Page Valuesc
		front_pg_df = pd.DataFrame([{"ndb_no":cur_line[1].text.strip(),"short_desc":cur_line[2].text.strip(),"manufac_fd_grp":cur_line[3].text.strip()}])
		# Merging food page and nutrient page dfs
		cur_food_df = pd.concat([front_pg_df, inner_pg_df], axis=1)
		# Appending to final dataframe
		page_df = page_df.append(cur_food_df, ignore_index=True)

	page_df['upc_num'] = page_df.short_desc.apply(lambda x: find_upc(x))
	page_df['desc_only'] = page_df.short_desc.apply(lambda x: remove_upc(x))
	page_df['unit_per_item_f'] = page_df['unit_per_item'].apply(lambda x: un_utf_8(x))
	page_df.to_csv('branded_foods_in_progress.csv', mode='a',index=False, header=False, index_label=0)
	return page_df

	

def parse_nutrient_page(food_url):
	# Download page and turn into Soup
	while True:
		try:
			newpage = requests.get(food_url)
			break
		except:
			time.sleep(20)
	ctr=0
	while(newpage.status_code!=200):
		if ctr>10&ctr<20:
			time.sleep(15)
		elif ctr>=20:
			break
		time.sleep(3)
		newpage = requests.get(food_url)
		ctr+=1 
	np_soup = BeautifulSoup(newpage.text, 'html.parser')
	col_12_list =  np_soup.findAll(attrs={"class":"col-md-12"})
	try:
		text_only = col_12_list[len(col_12_list)-1].text.strip()
		ingredients_list_df = pd.DataFrame([{'ingredients_list':re.split(r'\t',text_only)[1].strip()}])
	except:
		ingredients_list_df = pd.DataFrame([{'ingredients_list':np.nan}])
	# Get Per Unit Amt in Df
	headers = np_soup.findAll('th')
	columns_len = len(headers)
	if columns_len <4:
		unit_per_item_df = pd.DataFrame([{'unit_per_item':np.nan}])
	else:
		try:
			unit_per_item_df = pd.DataFrame([{'unit_per_item':headers[3].text.encode('UTF-8').strip()}])
		except:
			try: 
				unit_per_item_df = pd.DataFrame([{'unit_per_item':headers[3].text.encode('ISO-8859-1').strip()}])
			except:
				unit_per_item_df = pd.DataFrame([{'unit_per_item':np.nan}])
	# Parse Table Rows Into Long Df
	nutrients = []
	unit = []
	nut_scale_amt = []
	grams_100_amt = []
	row_list = np_soup.findAll('td')
	for i in range(0,len(row_list)):
		label = row_list[i].text.strip()
		if i%columns_len ==1:
			if '\n' in label:
				label = re.split(r'\n',label)[0]
			nutrients.append(label)
		elif i%columns_len==2:
			unit.append(label)
		elif i%columns_len==3:
			nut_scale_amt.append(label)
		elif i%columns_len==4:
			grams_100_amt.append(label)

	column_name_results = [column_name_lookup[nut] for nut in nutrients]
	if 'kj' in unit:
		column_name_results[unit.index] = 'kilojoules'
	per_unit_df = pd.DataFrame([dict(zip(column_name_results, nut_scale_amt))])
	food_pg_df = pd.concat([ingredients_list_df,unit_per_item_df, per_unit_df],axis=1)
	return food_pg_df

def crawl_pages():
	# Starting on first page
	start_url = 'https://ndb.nal.usda.gov/ndb/search/list'
	page_start = requests.get(start_url)
	soup_obj = BeautifulSoup(page_start.text,'html.parser')
	page_nums = soup_obj.findAll('a',attrs={"class":"step"})
	# Scraping First Page
	final_df = parse_foods_page(start_url)
	final_df.to_csv('branded_foods_in_progress.csv',index=False)
	# Getting How Many Pages To Parse
	nums_vec = []
	for num in page_nums:
		nums_vec.append(int(num.text))
	last_page = max(nums_vec)

	url_head = 'https://ndb.nal.usda.gov/ndb/search/list?maxsteps=6&format=&count=&max=50&sort=fd_s&fgcd=&manu=&lfacet=&qlookup=&ds=&qt=&qp=&qa=&qn=&q=&ing=&offset='
	url_tail = '&order=asc'
	for i in range(1,(last_page)):
	#for i in range(1,3): # For testing purposes
		loop_url = url_head + str(i*50)+url_tail
			# Get same thing here
		page_set = parse_foods_page(loop_url)
			# Append a dataframe

		print("Page "+str(i)+" crawled")

	return print('Page Crawl Action Complete')

def find_upc(x):
    try: 
        y = re.split('UPC:',x)[1].strip()
    except: 
        y = np.nan
    return y

def remove_upc(x):
    try:        
        y = re.split('UPC:',x)[0].strip()
    except: 
        y = x
    return y

def un_utf_8(text):
    text = text.replace('\\xc2\\xa0',u' ')
    text = text.replace("b'",u'')
    text = text.replace("'",u'')
    return text

pages_result = crawl_pages()



