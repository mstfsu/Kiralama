from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .filters import *

# Create your views here.

class IHAViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of IHA model"""
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filtering queryset by category"""
        queryset = self.queryset
        if self.request.GET.get('category'):
            queryset = queryset.filter(category__id=self.request.GET.get('category'))
        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    # def create(self, validated_data):
    #     """ Create IHA """
    #     print(type(validated_data.POST.get('category')))
    #     return Response({}, status.HTTP_200_OK)
class CategoryViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of Category model """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class BrandViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of Brand model """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BrandFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class DashboardStatics(APIView):
    def get(self, request):
        """ Get dashboard statics """
        total = IHA.objects.count()
        total_category = Category.objects.count()
        total_brand = Brand.objects.count()
        response_data = {
            'total_iha': total,
            'total_category': total_category,
            'total_brand': total_brand
        }
        return Response(response_data, status.HTTP_200_OK)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)