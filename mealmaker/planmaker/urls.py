from django.conf.urls import url
from .views import add_ingredient, add_recipe, add_plan, view_plans

urlpatterns = [
	url(r'add_ingredients', add_ingredient),
	url(r'add_recipe',add_recipe),
	url(r'add_plan',add_plan),
	url(r'show_plans',view_plans),
    ]