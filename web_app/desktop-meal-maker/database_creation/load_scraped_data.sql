

CREATE TABLE diet_facts_brands (
  brand_name varchar(55), /* Longest current length is 42 */
  calcium_perc numeric(10,2),/* post-processing to strip out %, < and long text (bugs)*/
  calories numeric(10,2),
  carb_g numeric(10,2),
  cholesterol_mg numeric(10,3),
  fat_g numeric(10,2),
  fiber_g numeric(10,2),
  iron_perc numeric(10,2),
  item_desc varchar(205), /*Longest current length is 200 - adding 5 for unencoding */
  item_name varchar(105), /*Longest current length is 100 - adding 5 for unencoding*/
  potassium_mg numeric(10,3),
  protein_g numeric(10,2),
  saturated_fat_g numeric(10,2),
  serving_size varchar(100), /*Longest full serving size is 66 - will just have to split this off as a full 'unit' and have 1 as the serving size in the unified db */
  sodium_mg numeric(10,3),
  sugar_g numeric(10,2),
  trans_fat_g numeric(10,2),
  vit_a_perc numeric(10,2),
  vit_c_perc numeric(10,2),
  brand_label varchar(50), /*Longest is 41 */
  category varchar(30) /*My own classification*/
)

/*Copy from post-processed csv */
\copy diet_facts_brands (brand_name, calcium_perc, calories, carb_g, cholesterol_mg, fat_g, fiber_g, iron_perc, item_desc, item_name, potassium_mg, protein_g, saturated_fat_g,serving_size, sodium_mg,sugar_g,trans_fat_g,vit_a_perc,vit_c_perc,brand_label,category) FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/diet_facts_df_formatted.csv'  CSV HEADER DELIMITER ',';
\copy diet_facts_brands FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/diet_facts_df_formatted.csv'  CSV HEADER;



CREATE TABLE branded_food_db (

	ndb_no int NOT NULL PRIMARY KEY,
	short_desc varchar(250), /*max length is 240 so far*/
	manufac_fd_grp varchar(100), /*max length is 79*/
	upc_num varchar(30), /*Upc numbers are 15 chars long, but some irregularities - will load them up and clean in sql */
	desc_only varchar(250), /*Max length is 233*/
	ingredients_list text,
	unit_per_item varchar(150),/*max length is 131*/
	/*Nutrients from usda nutritional db*/
	water numeric(10,2),
	kilocalories numeric(10),
	protein_g numeric(10,2),
	fat_g numeric(10,2),
	ash_g numeric(10,2),
	carb_g numeric(10,2),
	fiber_g numeric(10,1),
	sugar_g numeric(10,2),
	calcium_mg numeric(10),
	iron_mg numeric(10,2),
	magnesium_mg numeric(10),
	phosphorus_mg numeric(10),
	potassium_mg numeric(10),
	sodium_mg numeric(10),
	zinc_mg numeric(10,2),
	copper_mg numeric(10,3),
	manganese_mg numeric(10,3),
	selenium_mcg numeric(10,1),
	vit_c_mg numeric(10,1),
	thiamin_mg numeric(10,3),
	riboflavin_mg numeric(10,3),
	niacin_mg numeric(10,3),
	panto_acid_mg numeric(10,3),
	vit_b6_mg numeric(10,3),
	folate_mcg numeric(10),
	folic_acid_mcg numeric(10),
	food_folate_mcg numeric(10),
	folate_mcg_dfe numeric(10),
	choline_mg numeric(10),
	vit_b12_mcg numeric(10,2),
	vit_a_iu numeric(10),
	vit_a_mcg_rae numeric(10),
	retinol_mcg numeric(10),
	alpha_carotene_mcg numeric(10),
	beta_carotene_mcg numeric(10),
	beta_cryptoxanthin_mcg numeric(10),
	lycopene_mcg numeric(10),
	lutein_zeazanthin_mcg numeric(10),
	vit_e_mg numeric(10,2),
	vit_d_mcg numeric(10,1),
	vit_d_ui numeric(10),
	vit_k_mcg numeric(10,1),
	saturated_fatty_acid_g numeric(10,3),
	monosaturated_fatty_acid_g numeric(10,3),
	polysaturated_fatty_acid_g numeric(10,3),
	cholesterol_mg numeric(10,3),
	gm_weight_1 numeric(9,2),
	gm_weight_desc1 varchar(120),
	gm_weight_2 numeric(9,2),
	gm_weight_desc2 varchar(120),
	refuse_pct numeric(2),
	/* Added from usda branded foods db */
	kilojoules numeric(10,3),
	sucrose_g numeric(10,3),
	glucose_g numeric(10,3),
	fructose_g numeric(10,3),
	lactose_g numeric(10,3),
	maltose_g numeric(10,3),
	galactose_g numeric(10,3),
	starch_g numeric(10,3),
	flouride_mcg numeric(10,3),
	betaine_mg numeric(10,3),
	/* Making into a second column and can total into a full column in the model */
	vit_b12_added_mcg numeric(10,3),
	vit_e_added_mg numeric(10,3),
	beta_tocopherol_mg numeric(10,3),
	gamma_tocopherol_mg numeric(10,3),
	delta_tocopherol_mg numeric(10,3),
	alpha_tocopherol_mg numeric(10,3),
	beta_tocotrienol_mg numeric(10,3),
	gamma_tocotrienol_mg numeric(10,3),
	delta_tocotrienol_mg numeric(10,3),
	vit_d2_mcg numeric(10,3),
	vit_d3_mcg numeric(10,3),
	dihydrophylloquinone_mcg numeric(10,3),
	menaquinone_4_mcg numeric(10,3),
	ratio_4_0_g numeric(10,3),
	ratio_6_0_g numeric(10,3),
	ratio_8_0_g numeric(10,3),
	ratio_10_0_g numeric(10,3),
	ratio_12_0_g numeric(10,3),
	ratio_13_0_g numeric(10,3),
	ratio_14_0_g numeric(10,3),
	ratio_15_0_g numeric(10,3),
	ratio_16_0_g numeric(10,3),
	ratio_17_0_g numeric(10,3),
	ratio_18_0_g numeric(10,3),
	ratio_20_0_g numeric(10,3),
	ratio_22_0_g numeric(10,3),
	ratio_24_0_g numeric(10,3),
	ratio_14_1_g numeric(10,3),
	ratio_15_1_g numeric(10,3),
	ratio_16_1_undif_g numeric(10,3),
	ratio_16_1_c_g numeric(10,3),
	ratio_16_1_t_g numeric(10,3),
	ratio_17_1_g numeric(10,3),
	ratio_18_1_undif_g numeric(10,3),
	ratio_18_1_c_g numeric(10,3),
	ratio_18_1_t_g numeric(10,3),
	ratio_18_2_undif_g numeric(10,3),
	ratio_18_2_n_6_cc_g numeric(10,3),
	ratio_18_2_cla_g numeric(10,3),
	ratio_18_2_t_t_g numeric(10,3),
	ratio_18_2_i_g numeric(10,3),
	ratio_18_2_not_def_g numeric(10,3),
	ratio_18_3_undif_g numeric(10,3),
	ratio_18_3_n3_ccc_g numeric(10,3),
	ratio_18_3_n6_ccc_g numeric(10,3),
	ratio_18_3_i_g numeric(10,3),
	ratio_18_4_g numeric(10,3),
	ratio_20_2_n6_cc_g numeric(10,3),
	ratio_20_3_undif_g numeric(10,3),
	ratio_20_3_n3_g numeric(10,3),
	ratio_20_3_n6_g numeric(10,3),
	ratio_20_4_undif_g numeric(10,3),
	ratio_20_4_n6_g numeric(10,3),
	ratio_20_5_n3_epa_g numeric(10,3),
	ratio_21_5_g numeric(10,3),
	ratio_22_4_g numeric(10,3),
	ratio_22_5_n3_dpa_g numeric(10,3),
	ratio_22_6_n3_dha_g numeric(10,3),
	trans_fatty_acid_g numeric(10,3),
	trans_monoenoic_fatty_acid_g numeric(10,3),
	trans_polyenoic_fatty_acid_g numeric(10,3),
	phytosterols_mg numeric(10,3),
	stigmasterol_mg numeric(10,3),
	campesterol_mg numeric(10,3),
	beta_sitosterol_mg numeric(10,3),
	tryptophan_g numeric(10,3),
	threonine_g numeric(10,3),
	isoleucine_g numeric(10,3),
	leucine_g numeric(10,3),
	lysine_g numeric(10,3),
	methionine_g numeric(10,3),
	cystine_g numeric(10,3),
	phenylalanine_g numeric(10,3),
	tyrosine_g numeric(10,3),
	valine_g numeric(10,3),
	arginine_g numeric(10,3),
	histidine_g numeric(10,3),
	alanine_g numeric(10,3),
	aspartic_acid_g numeric(10,3),
	glutamic_acid_g numeric(10,3),
	glycine_g numeric(10,3),
	proline_g numeric(10,3),
	serine_g numeric(10,3),
	hydroxyproline_g numeric(10,3),
	ethyl_alcohol_g numeric(10,3),
	caffiene_mg numeric(10,3),
	theobromine_mg numeric(10,3)
)


\copy branded_food_db FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/usda_branded_formatted.csv' CSV HEADER;

CREATE TABLE fat_secret_all_search

(
	brand varchar(50),
	food varchar(200),
    food_type varchar(50),
	calcium_perc numeric(10,2),
	calories numeric(10,2),
	carb_g numeric(10,2),
	cholesterol_mg numeric(10,3),
	fat_g numeric(10,2),
	fiber_g numeric(10,2),
	iron_perc numeric(10,2),
	protein_g numeric(10,2),
	saturated_fat_g numeric(10,2),
	serving_size varchar(100), /*Longest full serving size is 88 */
	sodium_mg numeric(10,3),
	sugar_g numeric(10,2),
	vit_a_perc numeric(10,2),
	vit_c_perc numeric(10,2)
)

\copy fat_secret_all_search FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_all_search_formatted.csv' CSV HEADER;

CREATE TABLE fat_secret_recipes

(
	recipe_desc varchar(250),
	recipe_name varchar(100),
    full_ingred_list text,
	ingredient_list text,
	instructions text,
	meal_type varchar(100),
	quantities_list text,
	yield numeric(10,2),
    calcium_perc numeric(10,2),
	calories numeric(10,2),
	carb_g numeric(10,2),
	cholesterol_mg numeric(10,3),
	fat_g numeric(10,2),
	fiber_g numeric(10,2),
	iron_perc numeric(10,2),
	protein_g numeric(10,2),
	saturated_fat_g numeric(10,2),
	serving_size varchar(100), /*Longest full serving size is 88 */
	sodium_mg numeric(10,3),
	sugar_g numeric(10,2),
	vit_a_perc numeric(10,2),
	vit_c_perc numeric(10,2)
)

\copy fat_secret_recipes FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_recipe_formatted.csv' CSV HEADER;

CREATE TABLE fat_secret_full
(
	brand varchar(50),
	food varchar(200),
    food_type varchar(50),
	calcium_perc numeric(10,2),
	calories numeric(10,2),
	carb_g numeric(10,2),
	cholesterol_mg numeric(10,3),
	fat_g numeric(10,2),
	fiber_g numeric(10,2),
	iron_perc numeric(10,2),
	protein_g numeric(10,2),
	saturated_fat_g numeric(10,2),
	serving_size varchar(150), /*Longest full serving size is 88 */
	sodium_mg numeric(10,3),
	sugar_g numeric(10,2),
	vit_a_perc numeric(10,2),
	vit_c_perc numeric(10,2)
)
\copy fat_secret_full FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_full_formatted.csv' CSV HEADER;

CREATE TABLE fat_secret_alcohol
(
	brand varchar(50),
	food varchar(200),
    food_type varchar(50),
	calcium_perc numeric(10,2),
	calories numeric(10,2),
	carb_g numeric(10,2),
	cholesterol_mg numeric(10,3),
	fat_g numeric(10,2),
	fiber_g numeric(10,2),
	iron_perc numeric(10,2),
	protein_g numeric(10,2),
	saturated_fat_g numeric(10,2),
	serving_size varchar(100), /*Longest full serving size is 88 */
	sodium_mg numeric(10,3),
	sugar_g numeric(10,2),
	vit_a_perc numeric(10,2),
	vit_c_perc numeric(10,2)
)
\copy fat_secret_alcohol FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_alcohol_formatted.csv' CSV HEADER;

CREATE TABLE fat_secret_food_groups

(
	food varchar(200),
    food_group varchar(200),
    food_label varchar(200),
    food_sub_group varchar(200),
	calcium_perc numeric(10,2),
	calories numeric(10,2),
	carb_g numeric(10,2),
	cholesterol_mg numeric(10,3),
	fat_g numeric(10,2),
	fiber_g numeric(10,2),
	iron_perc numeric(10,2),
	protein_g numeric(10,2),
	saturated_fat_g numeric(10,2),
	serving_size varchar(100), /*Longest full serving size is 88 */
	sodium_mg numeric(10,3),
	sugar_g numeric(10,2),
	vit_a_perc numeric(10,2),
	vit_c_perc numeric(10,2)
)

\copy fat_secret_food_groups FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/fat_secret_groups_formatted.csv' CSV HEADER;
