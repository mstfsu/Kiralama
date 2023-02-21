from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import IHA
from .serializers import IHASerializer
from .filters import IHAFilter
# Create your views here.

class IHAViewSet(viewsets.ModelViewSet):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    #permission_classes = [IsAuthenticated]