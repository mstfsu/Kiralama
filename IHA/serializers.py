from rest_framework import serializers
import json
from .models import IHA, Brand, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        datatables_always_serialize = ('id',)

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        datatables_always_serialize = ('id',)

class IHASerializer(serializers.ModelSerializer):
    class Meta:
        model = IHA
        fields = "__all__"
        datatables_always_serialize = ('id',)

    def to_internal_value(self, data):
        if type(data) is not  dict:
            data = data.dict()
        if type(data['category']) is  str:
            data['category'] = [int(x) for x in data['category'].split(',')]
        return super().to_internal_value(data)

    def to_representation(self, instance):
        self.fields['brand'] =  BrandSerializer(read_only=True)
        self.fields['category'] = CategorySerializer(many=True, read_only=True)
        return super(IHASerializer, self).to_representation(instance)

    