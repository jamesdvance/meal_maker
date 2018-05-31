/* 'Foods' backend database for Django Application */
CREATE TABLE foods (
  food_key integer NOT NULL PRIMARY KEY,
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

\copy foods FROM 'C:/Users/J/Desktop/Businesses/Meal_Maker/Scraped_Data/combined_nutrition_small/nutrition_sm_processed_ss.csv' CSV HEADER;

