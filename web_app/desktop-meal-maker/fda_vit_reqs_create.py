



fda_reqs_sm =pd.DataFrame([{
	'calcium_mg': 1000,
	'iron_mg':18
	'vit_a_mcg':5000,
	'vit_c_mg':60,
	'sodium_mg': 2400 # less than
	}])

# FDA reqs - using usda grocery prod names
fda_reqs_full =pd.DataFrame([{
	# No biotin?
	'folate_mcg': 400, # Either / or
	'folic_acid_mcg': 400, # Either / or
	'niacin_mg':20,
	'panto_acid_mg': 10,
	'riboflavin_mg': 1.7,
	'thiamin_mg': 1.5,
	'vit_a_mcg':5000,
	'vit_b6_mg': 2,
	'vit_b12_mcg': 6,
	'vit_c_mg':60,
	'vit_d_ui': 400, # either / or
	'vit_d_mcg': 10,
	'vit_e_mg':22, #used online converter
	'vit_k_mcg': 80,
	'calcium_mg': 1000,
	# No chloride?
	# No chromium?
	'copper_mg': 2,
	# No iodine?
	'iron_mg':18,
	'magnesium_mg':400,
	'manganese_mg': 2,
	# No molybdenum?
	'phosphorus_mg':1000,
	'potassium_mg':3500,
	'selenium_mcg': 70,
	'sodium_mg': 2400, # less than
	'zinc_mg':15

	}])

#fda_pregnant_reqs # need biotins