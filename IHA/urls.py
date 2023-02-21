
from django.urls import path
from .views import *

iha_list = IHAViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

iha_detail = IHAViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

brand_list = BrandViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

brand_detail = BrandViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', iha_list, name='iha-list'),
    path('<int:pk>/', iha_detail, name='iha-detail'),
    path('category/', category_list, name='category-list'),
    path('category/<int:pk>/', category_detail, name='category-detail'),
    path('brand/', brand_list, name='brand-list'),
    path('brand/<int:pk>/', brand_detail, name='brand-detail'),
    path('dashboard-statics/', DashboardStatics.as_view(), name='dashboard-statics'),
]
