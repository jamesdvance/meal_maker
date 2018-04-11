from django.contrib import admin
from .models import Ingred, Recipe, DailyPlan

# Register your models here.

admin.site.register(Ingred)
admin.site.register(Recipe)
admin.site.register(DailyPlan)