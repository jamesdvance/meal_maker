
# Basic Built-In Reqs
# 

def food_grp_reqs():

    import pandas as pd
    fd_grps = pd.read_csv("C:/Users/J/Desktop/Businesses/Meal_Maker/Food Classifications/usda_food_groups.csv")

    groups = fd_grps['Group'].unique()
    subgroups = fd_grps['Subgroup'].unique()

    # For each food group, need the Group Column, Group Name, Amount (float or int), and recurrance (by meal, daily or weekly)
    # In the interface, they should be able to click into food groups, food subgroups, and other categories.
    # Should add an ability to look up custom tag groups and add
    print(subgroups)
    grp = input("Which group would you like to add to rules? ")
    recurrance = input("How often would you like this item in your diet? Choices are Breakfast, Lunch, Dinner, Daily, Weekly. ")
    amount = input("How much would you like at that recurrance? ")

    grp_df = pd.DataFrame([{"group_column":"usda_subgroup", "group_val":grp, "recurrance":recurrance, "amount":amount}])
    return grp_df


def other_nutrition_reqs():
# Nutritional Requirements that aren't macros or 
# Indicate the nutrient you would like in your diet at some regular interval.
# Can follow same format as above
	return None

def vitamin_mineral_reqs(cal_reqs):
# Nutritional Requirements related to vitamins and minerals such as vit a, calcium, iron, etc 
    import pandas as pds
# Should adjust suggested amounts based on 2k cal diet to individual cal_reqs
    recurrance = input("Would you like to follow the usda vitamin recommendations? ")
    amount = input("How many times should this met during that time period?")

    nut_df = pd.DataFrame([{"req":"usda_all_vit", "recurrance":recurrance, "amount":amount, "cal_req":cal_reqs}])

    return nut_df


