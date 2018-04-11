

def calc_bmr():
    age_dict = {'male':5, 'female':-161}

    weight = float(input("How Much Do You Weigh (in pounds)? "))
    height = float(input("How Tall Are You (in inches)? "))
    sex = input("Are you male or female? ")
    age = float(input("How old are you (years)? "))
    # Conversions
    kg_w = weight/2.204623
    cm_h = height*2.54
    age_fac = age_dict[sex]

    bmr = 10*kg_w+6.25*cm_h-5*age+age_fac
    return bmr

def calc_tdee(bmr=None):
    activity_dict = {1:1.2, 2:1.375, 3:1.55,4:1.725,5:1.9}

    if bmr == None:
        bmr=calc_bmr()

    print("Exercise Level 1: Little or no exercise w/ a desk job.")
    print("Exercise Level 2: Light exercise or sport 1-3 days/ week. Sedentary otherwise.")
    print("Exercise Level 3: Moderate exercise or sport 3-5 days a week")
    print("Exercise Level 4: Heavy Exercise or sport 6-7 days a week.")
    print("Exercise Level 5: I'm a physical animal. If I'm not doing 2-a-day workouts I'm working a demanding physical job.")

    activity_lvl = int(input("Which of these best describes your exercise level? Please enter a numbers?"))
    act_adj = activity_dict[activity_lvl]
    tdee = bmr * act_adj 

    return tdee

def 