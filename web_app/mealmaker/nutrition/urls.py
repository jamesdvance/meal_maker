from django.conf.urls import url
from .views import add_requirements, show_requirements

urlpatterns = [
	url(r'^$', add_requirements),
	url(r'show', show_requirements),
	]


