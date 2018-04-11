/* For space constraints, will create one consolidated nutrition db with standard, but not detailed fields. 

item data: name, description (optional), ingredients (optional), serving size, serving size unit

nutritient data: calories, fat, carbs, protein, fiber, sugars, saturated fat, sodium, cholesterol

group data: food type {raw ingredient, grocery food, restaurant food, recipe}, usda food group (optional)


/* Then will create an all-inclusive database for specialized needs - nutrition_bg, also maybe nutrition_vit for vitamins only */

CREATE TABLE nutrition_sm (
  /* Food Attributes */
  food_key serial NOT NULL PRIMARY KEY,
  food_description varchar(350),
  brand varchar(250),
  food_type_grp varchar(30), /*Seems important enough to have in this first table*/
  source varchar(50),
  ingredients_list text,
  serving_size_raw varchar(200),
  serving_size_val numeric(10,2),
  serving_size_unit varchar(200),
  /* Nutrition Attributes */
  calories numeric(10),
  protein_g numeric(10,2),
  fat_g numeric(10,2),
  saturated_fat_g numeric(10,2),
  carb_g numeric(10,2),
  fiber_g numeric(10,2),
  sugar_g numeric(10,2),
  sodium_mg numeric(10,2),
  cholesterol_mg numeric(10,3),
  calcium_mg numeric(10,2), /*1k mg */
  iron_mg numeric(10,2), /* 18 mg */
  vit_a_mcg numeric(10,2), /*5k mcg */
  vit_c_mg numeric(10,2) /*60 mg */
)
/* Can create a seperate 'extra' vitamins table */
/* Should probably just have all vit a, vit c, calcium, and iron*/
CREATE TABLE food_grps AS (

  food_key NOT NULL,
  food_type_grp varchar(30), /* ingredient, grocery, restaurant, recipe */
  purchase_source_grp varchar(30), /*Whole Foods, restaurants, raw ingredient (is its own group and is considered an always-available grocery stores) */
  meal_type_grp varchar(30) /* all_meals, breakfast_only, non_breakfast, snack_only, lunch_only, dinner_only, non_lunch */
  /*Much more can be added, including prep time, usda food groups, and high-nutrient foods*/
 
)

CREATE TABLE purchase_grps AS (
  
   purchase_grp_key serial primary key
   
)

CREATE TABLE recipe_details AS (
  food_key not null,
  yield numeric(10,2)
  ingredients_list text, /*Not doing array bc of comma-seperated problems*/
  quantities_list text,
  instructions text,
  recipe_type text
)