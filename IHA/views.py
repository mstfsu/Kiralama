from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .filters import *

# Create your views here.


class IHAViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of IHA model
        create, update, delete, list, retrieve
    """
    queryset = IHA.objects.all()
    serializer_class = IHASerializer

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        """Filtering queryset by category
            other seach filters are handled by DataTables
        """
        queryset = self.queryset
        if self.request.GET.get('category'):
            queryset = queryset.filter(
                category__id=self.request.GET.get('category'))
        return queryset

    # def create(self, validated_data):
    #     """ Create IHA """
    #     pass
       
        #return Response({}, status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of Category model 
        create, update, delete, list, retrieve
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """ Check if user is authenticated """
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        """Filtering queryset by name"""
        queryset = self.queryset
        if self.request.GET.get('search[value]'):
            queryset = queryset.filter(
                name__icontains=self.request.GET.get('search[value]'))
        return queryset


class BrandViewSet(viewsets.ModelViewSet):
    """ ViewSet for crud operations of Brand model 
        create, update, delete, list, retrieve
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BrandFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """ Check if user is authenticated """
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        """Filtering queryset by name"""
        queryset = self.queryset
        if self.request.GET.get('search[value]'):
            queryset = queryset.filter(
                name__icontains=self.request.GET.get('search[value]'))
        return queryset


class DashboardStatics(APIView):
    def get(self, request):
        """ Get dashboard statics """
        total = IHA.objects.count()
        total_category = Category.objects.count()
        total_brand = Brand.objects.count()
        total_user = User.objects.count()
        response_data = {
            'total_iha': total,
            'total_category': total_category,
            'total_brand': total_brand,
            'total_user' : total_user
        }
        return Response(response_data, status.HTTP_200_OK)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """ Check if user is authenticated """
        return super().dispatch(*args, **kwargs)
