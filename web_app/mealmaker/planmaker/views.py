from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from planmaker.models import Ingred, Recipe,DailyPlan
from nutrition.models import Nutrition_Req
from .forms import IngredForm, RecipeForm, DailyPlanForm
from django.db import connection
from django.db.models import Q, F, Min, Sum
# Create your views here.
# Login

# Add Ingredient
@login_required(login_url='/')
def add_ingredient(request):	
	if request.method == 'POST':
		form = IngredForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.submit_user = request.user
			model_instance.save()
			if model_instance.standalone ==True:
				recipe_instance = Recipe(
										submit_user=request.user,
										prep_time = 'none',
										recipe_name = model_instance.ingred_name
										)
				recipe_instance.save()
				recipe_instance.ingred.add(model_instance.id)
			return HttpResponseRedirect('/')
	else:
		form = IngredForm()
		return render(request,'add_ingred_form.html',{'form':form})

@login_required(login_url='/')
def add_recipe(request): # Should return a form to submit a recipe, and a list of ten ingredients (which auto-refreshes when an ingredient is added)
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.submit_user = request.user
			model_instance.save()
			form.save_m2m()
			return HttpResponseRedirect('/')
	else: 
		form = RecipeForm()
		#custom_ingred_choices = Ingred.objects.filter(submit_user = request.user)[:10]# order_by("uses")Should customize this to be most used by the user
		return render(request, 'add_recipe_form.html', {'form': form})

# This view should display most recent 10 plans (and be searchable), have a plan form, and have a weekly plan form (drag and drop eventually) and someday show recipe recommendations while building plan
@login_required(login_url='/')
def add_plan(request):
	if request.method=='POST':
		form = DailyPlanForm(request.POST)
		if form.is_valid():
			plan_instance = form.save(commit=False)
			plan_instance.user = request.user
			plan_instance.save()
			form.save_m2m()
			return HttpResponseRedirect('/') # Eventaully want to display return to same page with most recent plans displayed on side

	else:
		plan_form = DailyPlanForm()
		user_plans = DailyPlan.objects.filter(user=request.user).order_by('-created')[:10]
		return render(request, 'daily_plan_form.html', {'plan_form':plan_form, 'user_plans':user_plans})

# View all plans 
@login_required(login_url='/')
def view_plans(request):
	plans = DailyPlan.objects.raw('SELECT dp.plan_id, sum(i.cal) as total_cals, sum(i.carbs) as total_carbs, sum(i.fat) as total_fat, sum(i.protein) as total_protein FROM DailyPlan dp  JOIN recipe r ON (   dp.breakfast = r.recipe_id OR dp.mid_morning_snack = r.recipe_id OR dp.lunch = r.recipe_id OR dp.afternoon_snack = r.recipe_id OR dp.dinner = r.recipe_id OR dp.after_dinner_snack = r.recipe_id) JOIN ingred i ON r.ingred = i.ingred_id GROUP BY 1')
	reqs = Nutrition_Req.objects.filter(user=request.user)
	'''
	for plan in plans:

		carb_diff = abs(plan.total_carbs -reqs[0].total_carb)
	'''

	return render(request, 'show_plan_totals.html', {'plans':plans, 'reqs':reqs})
	