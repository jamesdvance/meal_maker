

/* Loading from usda branded */

INSERT INTO nutrition_sm 
(
  food_description,
  brand,
  food_type_grp,
  ingredients_list,
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
) 
SELECT 
  desc_only,
  manufac_fd_grp,
  cast('grocery' as varchar(30)) as food_type_grp,
  ingredients_list,
  cast('usda_branded' as varchar(30)) as source,
  unit_per_item,
  kilocalories,
  protein_g,
  fat_g,
  saturated_fatty_acid_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg,
  iron_mg,
  vit_a_mcg_rae,
  vit_c_mg

FROM branded_food_db

/*Loading from diet facts */
INSERT INTO nutrition_sm 
(
  food_description,
  brand,
  food_type_grp,
  ingredients_list,
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
) 
SELECT 
  item_name,
  brand_label,
  case when category = 'brand' then cast('grocery'as varchar(30)) else category end as food_type_grp,
  item_desc,
  case when category = 'brand' then  cast('diet_facts_brands' as varchar(30)) else cast('diet_facts_restaurants' as varchar(30)) end as source,
  serving_size,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_perc * .01 * 1000 as calcium_mg,
  iron_perc * .01 * 18 as iron_mg,
  vit_a_perc * .01* 5000 as vit_a_mcg,
  vit_c_perc * .01* 60 as vit_c_mg
FROM diet_facts_brands
/*Loading from raw ingredients */

INSERT INTO nutrition_sm 
(
  food_description,
  brand,
  food_type_grp,
  ingredients_list,
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
) 
SELECT 
  short_desc,
  cast('raw ingredient' as varchar(250)) as brand,
  cast('raw ingredient' as varchar(30)) as food_type_grp,
  short_desc,
  cast('usda_raw_ingred' as varchar(30)) as source,
  gm_weight_desc1,
  kilocalories*0.01*food_nutrients.gm_weight_1 as calories, 
  protein_g*0.01*food_nutrients.gm_weight_1 as protein_g,
  fat_g*0.01*food_nutrients.gm_weight_1 as fat_g,
  saturated_fatty_acid_g*0.01*food_nutrients.gm_weight_1 as saturated_fat_g,
  carb_g*0.01*food_nutrients.gm_weight_1 as carb_g,
  fiber_g*0.01*food_nutrients.gm_weight_1 as fiber_g,
  sugar_g*0.01*food_nutrients.gm_weight_1 as sugar_g,
  sodium_mg*0.01*food_nutrients.gm_weight_1 as sodium_mg,
  cholesterol_mg*0.01*food_nutrients.gm_weight_1 as cholesterol_mg,
  calcium_mg*0.01*food_nutrients.gm_weight_1 as calcium_mg,
  iron_mg*0.01*food_nutrients.gm_weight_1 as iron_mg,
  vit_a_mcg_rae *0.01*food_nutrients.gm_weight_1 as vit_a_mcg,
  vit_c_mg *0.01*food_nutrients.gm_weight_1 as vit_c_mg

FROM food_nutrients

/* Diet Facts 'all' search */

INSERT INTO nutrition_sm (
  food_description,
  brand,
  food_type_grp,
 /* ingredients_list,*/
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
) 

SELECT
  food,
  cast('raw ingredient' as varchar(250)) as brand,
  cast('raw ingredient' as varchar(30)) as food_type_grp,
  cast('fat_secret_all_search' as varchar(30)) as source,
  serving_size,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_perc * .01 * 1000 as calcium_mg,
  iron_perc * .01 * 18 as iron_mg,
  vit_a_perc * .01* 5000 as vit_a_mcg,
  vit_c_perc * .01* 60 as vit_c_mg

FROM fat_secret_all_search


/* Diet Facts Recipes */

INSERT INTO nutrition_sm
(
  food_description,
  brand,
  food_type_grp,
  ingredients_list,
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
)

SELECT 
  recipe_name,
  cast('recipe' as varchar(30)) as brand,
  cast('recipe' as varchar(30)) as food_type_grp,
  ingredient_list,
  cast('fat_secret_recipes' as varchar(30)) as source,
  serving_size,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_perc * .01 * 1000 as calcium_mg,
  iron_perc * .01 * 18 as iron_mg,
  vit_a_perc * .01* 5000 as vit_a_mcg,
  vit_c_perc * .01* 60 as vit_c_mg


FROM fat_secret_recipes 


INSERT INTO nutrition_sm (
  food_description,
  brand,
  food_type_grp,
 /* ingredients_list,*/
  source,
  serving_size_raw,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_mg, /*1k mg */
  iron_mg, /* 18 mg */
  vit_a_mcg, /*5k mcg */
  vit_c_mg /*60 mg */
)

SELECT
  food,
  brand,
  food_type,
  cast('fat_secret' as varchar(30)) as source,
  serving_size,
  calories,
  protein_g,
  fat_g,
  saturated_fat_g,
  carb_g,
  fiber_g,
  sugar_g,
  sodium_mg,
  cholesterol_mg,
  calcium_perc * .01 * 1000 as calcium_mg,
  iron_perc * .01 * 18 as iron_mg,
  vit_a_perc * .01* 5000 as vit_a_mcg,
  vit_c_perc * .01* 60 as vit_c_mg


FROM fat_secret_full