import pandas as pd 

data = pd.read_csv("branded_foods_in_progress_150k.csv")

for i range(data):

	usda_df = Ingred(
		submit_user = 'usda_branded_foods',
		ingred_name = data.iloc[i,]
	)
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

usda_df.save()


def import_csv(request):
	file = 'scraping_branded_food_products/branded_foods'
	with open(file, 'rb') as csvfile:
		with closing(connections['database_name']).cursor()) as cursor:
			cursor.copy_from(
				file = csvfile,
				table=''
				)
