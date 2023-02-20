from rest_framework import serializers
from .models import IHA, Brand, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['brand'] =  BrandSerializer(read_only=True)
        self.fields['category'] = CategorySerializer(many=True, read_only=True)
        return super(IHASerializer, self).to_representation(instance)