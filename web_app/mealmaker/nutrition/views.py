from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from .models import  Nutrition_Req
from .forms import RequirementsForm
# Create your views here.

class Nutrition_ReqUpdate(UpdateView):
	model = Nutrition_Req
	fields = ['daily_cal', 'daily_carb','daily_fat','daily_protein', 'daily_sugar', 'flex_perc']
	template_name_suffix = '_update_form'

@login_required(login_url='/')
def add_requirements(request):
	try:
		requirements = Nutrition_Req.objects.get(user=request.user)

	except Nutrition_Req.DoesNotExist:

		if request.method == 'POST':
			form = RequirementsForm(request.POST) 
			if form.is_valid():
				model_instance = form.save(commit=False)
				model_instance.user = request.user
				model_instance.save()
				return HttpResponseRedirect('show/')

		else:
			form = RequirementsForm()
			return render(request, 'add_reqs_form.html', {'form':form})

	if request.method == 'POST':
		form = RequirementsForm(request.POST, instance = requirements)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.user = request.user
			model_instance.save()
			return HttpResponseRedirect('show/')

	else:
		form = RequirementsForm(instance = requirements)
		return render(request, 'add_reqs_form.html', {'form':form}) # Includes pre-populated form

@login_required(login_url='/')
def show_requirements(request):
	reqs = Nutrition_Req.objects.get(user=request.user)

	return render(request, 'show_reqs.html', {'reqs':reqs})

# Create your views here.
