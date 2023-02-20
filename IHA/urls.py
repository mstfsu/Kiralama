
from django.urls import path
from .views import IHAViewSet

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

urlpatterns = [
   path('', iha_list, name='iha-list'),
    path('<int:pk>/', iha_detail, name='iha-detail'),
]
