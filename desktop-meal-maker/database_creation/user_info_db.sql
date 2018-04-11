/* Whatup */

/*
CREATE TABLE AS (
  user_id serial primary key,
  username 

)
*/
CREATE TABLE user_nut_reqs AS (
	user_id not null,
	calories_req numeric(10,2),
	prot_g_req numeric(10,2),
	fat_g_req numeric(10,2),
	saturated_fat_g_req numeric(10,2),
	carb_g_req numeric(10,2),
	fiber_g_req numeric(10,2),
	sugar_g_req numeric(10,2),
    sodium_mg_req numeric(10,2),
    cholesterol_mg_req numeric(10,3),
    flex_perc numeric(10,2)
)

CREATE TABLE user_grp_reqs AS (
  user_id not null,
  food_grp varchar(30), /*food_type_grp, purchase_source_grp, meal_type_grp, etc */
  food_grp_val varchar(30) /*Value of the group */
)

CREATE TABLE user_like_dislike AS (
  user_id not null,
  food_key not null,
  like_flg not null varchar(1),
  rating smallint, /*Rate 1 - 5 */
  suggestion_cnt smallint,
  accept_cnt smallint,
)

/* Future state 
CREATE TABLE user_week_reqs AS (
  user_id not null,
  cheat_days smallint,
  cheat_cal_flex numeric(10,2),
  recipe_perc numeric(10,2),
  leftover_perc numeric(10,2),
  restaurant_perc numeric(10,2),
)
*/