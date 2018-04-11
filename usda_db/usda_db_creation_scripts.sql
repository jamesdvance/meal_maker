
/* Creation Scripts */

/* Create Food Description Table */

CREATE TABLE food_desc (

	ndb_no varchar(5) NOT NULL PRIMARY KEY,
	fd_grp_cd varchar(4) NOT NULL,
	long_desc varchar(200) NOT NULL,
	short_desc varchar(60) NOT NULL,
	com_name varchar(100),
	manufac_name varchar(65),
	survey varchar(1),
	ref_desc varchar(135),
	refuse smallint,
	sci_name varchar(65),
	n_factor numeric(4,2),
	pro_factor numeric(4,2),
	fat_factor numeric(4,2),
	cho_factor numeric(4,2)
)

/*loading into db*/
/* psql script */
\copy food_des FROM 'FOOD_DES.txt' (FORMAT CSV, DELIMITER '^', QUOTE '~');

CREATE TABLE food_grp_desc (
	fd_grp_cd varchar(4) NOT NULL PRIMARY KEY,
	fd_grp_desc varchar(60) NOT NULL
)

\copy food_grp_desc FROM 'C:/Users/J/Datasets/Nutrition/usda/sr28asc/FD_GROUP.txt' (FORMAT CSV, DELIMITER '^', QUOTE '~');

/* Getting a duplicate value error right now in trying to set the primary key on either field. Ommitting for now */
CREATE TABLE langual (

	ndb_no varchar(5) NOT NULL PRIMARY KEY,
	factor_cd varchar(5) NOT NULL
)

\copy langual FROM 'C:/Users/J/Datasets/Nutrition/usda/sr28asc/LANGUAL.txt' (FORMAT CSV, DELIMITER '^', QUOTE '~');

/* Also skipping the langual factors description file */

CREATE TABLE nutrient_data (

	ndb_no varchar(5) NOT NULL ,
	nut_no varchar(3) NOT NULL PRIMARY KEY,
	nut_val numeric(10,5) NOT NULL,
	num_data_pts numeric(5,0) NOT NULL,
	std_error numeric(8,3),
	src_cd varchar(2) NOT NULL,
	deriv_cd varchar(4),
	ref_ndb_no varchar(5),
	added_nut_ind varchar(1),
	num_studies smallint,
	min_amt numeric(10,3),
	max_amt numeric(10,3),
	deg_freedom smallint,
	low_eb numeric(10,3),
	up_eb numeric(10,3),
	stat_cmt varchar(10),
	date_added_or_modified varchar(10),
	confidence_code varchar(1)
)

\copy nutrient_data FROM 'C:/Users/J/Datasets/Nutrition/usda/sr28asc/NUT_DATA.txt' (FORMAT CSV, DELIMITER '^', QUOTE '~');

CREATE TABLE food_nutrients (

	ndb_no varchar(5) NOT NULL PRIMARY KEY,
	short_desc varchar(60),
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
	refuse_pct numeric(2)
)

CREATE DATABASE branded_food_db AS (

	ndb_no varchar(5) NOT NULL PRIMARY KEY,
	short_desc varchar(150),
	manufac_fd_grp varchar(100),
	upc_num varchar(15),
	desc_only varchar(150),
	ingredients_list text,
	unit_per_item varchar(100),
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

\copy food_nutrients FROM 'C:/Users/J/Datasets/Nutrition/usda/ABBREV.txt' (FORMAT CSV, DELIMITER '^', QUOTE '~');
