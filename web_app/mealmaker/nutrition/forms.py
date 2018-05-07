from nutrition.models import Nutrition_Req
from django.contrib.auth.models import User
from django.forms import ModelForm


class RequirementsForm(ModelForm):
	class Meta:
		model = Nutrition_Req
		fields = ['daily_cal', 'daily_carb','daily_fat','daily_protein', 'daily_sugar', 'flex_perc']

