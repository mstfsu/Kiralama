
from django.urls import path
from .views import *


urlpatterns = [
   path('index', index, name='index'),
   path('', dashboard, name='dashboard'),
   path('iha/create', create, name='create')
   ]
