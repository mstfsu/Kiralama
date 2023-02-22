
from django.urls import path
from .views import *


urlpatterns = [
   path('index', index, name='index'),
   path('', dashboard, name='dashboard'),
   path('iha/create', create, name='create'),
   path('category', category, name='category'),
   path('category/create', create_category, name='create_category'),
   path('brand', brand, name='brand'),
   path('brand/create', create_brand, name='create_brand'),
   ]
