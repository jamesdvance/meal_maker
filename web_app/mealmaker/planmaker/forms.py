
from planmaker.models import Ingred, Recipe, DailyPlan
from django.contrib.auth.models import User
from django.forms import ModelForm


class IngredForm(ModelForm):

	class Meta:
		model = Ingred
		fields = ['ingred_name', 'ingred_amt','ingred_unit','cal','carbs','fat','protein','sugar','min_amt','max_amt' , 'standalone']


class RecipeForm(ModelForm):
	class Meta: 
		model = Recipe
		fields = [ 'prep_time',  'ingred', 'recipe_name']

class DailyPlanForm(ModelForm):
	class Meta:
		model = DailyPlan
		fields = ['breakfast', 'mid_morning_snack','lunch', 'afternoon_snack','dinner','after_dinner_snack', 'nickname']

