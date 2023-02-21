from django_filters import filters
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter
from .models import IHA

class GlobalCharFilter(GlobalFilter, filters.CharFilter):
    pass

class IHAFilter(DatatablesFilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    weight = filters.NumberFilter(field_name='weight', lookup_expr='lte')   
   
     
    class Meta:
        model = IHA
        fields = ['name', 'weight']
   