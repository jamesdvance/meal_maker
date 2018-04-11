from django.db import models
from django.contrib.auth.models import User
import datetime

# Plan_Weeks
Days_of_Week = (
		('Monday', 'Monday'),

	)

# Plans
Meals = (
	('Breakfast', 'Breakfast'),
	('MMS', 'Mid Morning Snack'),
	('Lunch', 'Lunch'),
	('AS', 'Afternoon Snack'),
	('Dinner','Dinner'),
	('ADS', 'After Dinner Snack'),
	)

# Recipes
Dishes = (
	('Feature', 'Feature'),
	('Side', 'Side'),
	('Snack', 'Snack'),
	('Desert', 'Desert'),
	)

Prep_Times = (
	('long', 'long'),
	('short', 'short'),
	('none', 'none'),
	)

# Ingredients
Units = (
	('cup','cup'),
	('gram','gram'),
	('container', 'container'),
	('oz','oz'),
	('fl oz','fl oz'),
	('pnt','pnt'),
	('item','item'),
	('tblsp', 'tblsp'),
	)


def get_week_ending_list():
	today_date = datetime.date.today()
	weekday_today = today_date.weekday()
	if weekday_today == 5:
		week_ending_dt = today_date
	elif weekday_today < 5:
		week_ending_dt = today_date + datetime.timedelta((5-weekday_today))
	else:
		week_ending_dt = today_date + datetime.timedelta((12-weekday_today))
	week_list = (
		('this_week_ending', week_ending_dt),
		('next_week_ending', week_ending_dt+datetime.timedelta(7)),
		('two_weeks_ending', week_ending_dt+datetime.timedelta(14)),
		('three_weeks_ending',week_ending_dt+datetime.timedelta(21)),
		('four_weeks_ending', week_ending_dt+datetime.timedelta(28)),
		)
	return week_list

week_list = get_week_ending_list()
 
# Should ingredients have users or users have ingredients?
# Each user could have a many to one field of ingredients
class Ingred(models.Model):
	submit_user= models.ForeignKey(User) # Must keep ingredients even if a user deletes account
	ingred_name = models.CharField(max_length = 300) 
	ingred_amt = models.FloatField()
	ingred_unit = models.CharField(max_length=100, choices=Units) # Want to give choices here or they can add
	cal = models.FloatField()
	carbs = models.FloatField()
	fat = models.FloatField()
	protein = models.FloatField()
	sugar = models.FloatField()
	min_amt = models.FloatField()
	max_amt = models.FloatField()
	standalone = models.BooleanField(default=True)
	#recipe_uses = models.IntegerField()
	#cost = models.FloatField() # Should be optional
	# Could just have a field which, if selected automatically creates a recipe object as well with the same specs as the ingredient
	
	def __str__(self):
		return self.ingred_name

# Combine recipes and meals into one item?
# Recipes should have macros also
class Recipe(models.Model):
	submit_user = models.ForeignKey(User)
	recipe_name = models.CharField(max_length=300, default="Unnamed")
	prep_time = models.CharField(choices=Prep_Times, max_length=300, blank=True)
	ingred = models.ManyToManyField(Ingred)

	def __str__(self):
		return str(self.recipe_name)

# Should exist distinct for each user. If someone wants to copies others plans, can migrate the model


class DailyPlan(models.Model):
	user = models.ForeignKey(User) # Do not delete
	created = models.DateTimeField(auto_now_add = True) # DateTime of model created
	breakfast = models.ManyToManyField(Recipe, related_name='breakfast_recipes', blank=True)
	mid_morning_snack = models.ManyToManyField(Recipe, related_name = 'mid_morning_snack_recipes', blank=True)
	lunch = models.ManyToManyField(Recipe, related_name = 'lunch_recipes', blank=True)
	afternoon_snack = models.ManyToManyField(Recipe, related_name = 'afternoon_snack_recipes', blank=True)
	dinner = models.ManyToManyField(Recipe, related_name = 'dinner_recipes', blank=True)
	after_dinner_snack = models.ManyToManyField(Recipe, related_name = 'after_dinner_snack_recipes', blank=True)

	def _get_nth_plan(self):
		# Get total objects related to this user
		nth_plan = DailyPlan.get.filter(user=self.user).count() + 1
		return nth_plan

	def _get_users_nth(self):
		return str(self.user)+"_"+str(self.nth_plan)

	nth_plan = property(_get_nth_plan)
	users_nth = property(_get_users_nth) # would be nice if this was the default nick name, unless a person changes its
	nickname = models.CharField(max_length = 300, blank=True)
	
	def __str__(self):
		return str(self.user)+"_"+str((self.created))

