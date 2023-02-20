from django.shortcuts import render
from rest_framework import viewsets
from .models import IHA
from .serializers import IHASerializer
from base.pagination import StandardResultsSetPagination

# Create your views here.

class IHAViewSet(viewsets.ModelViewSet):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    pagination_class = StandardResultsSetPagination