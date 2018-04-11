from django.db import models
from django.contrib.auth.models import User


class Nutrition_Req(models.Model):
	user = models.OneToOneField(User, 
								on_delete=models.CASCADE,
								primary_key = True,)	
	daily_cal = models.IntegerField()
	daily_carb = models.IntegerField()
	daily_fat = models.IntegerField()
	daily_protein = models.IntegerField()
	daily_sugar = models.IntegerField(default = 40)
	flex_perc = models.FloatField(default=.005)
	
	def __str__(self):
			return str(self.user)