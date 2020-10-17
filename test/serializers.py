from rest_framework import serializers
from test.models import *


class goodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class subItemSerializer(serializers.ModelSerializer):
    goods = goodsSerializers(many=True)
    class Meta:
        model = SubItem
        fields = ('id','name','sub','goods')

class subCategorySeriazlier(serializers.ModelSerializer):
    items = subItemSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ('id','name','category','attributes','items')


class categorySerializer(serializers.ModelSerializer):
    subCategories = subCategorySeriazlier(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subCategories',)
