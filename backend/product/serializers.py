from rest_framework import serializers
from rest_framework.exceptions import server_error
from product.models import ProductCategory, SaleChannel, Topping, TypeTopping, PriceTopping, TableTopping, Product, PriceProduct
from django.http import request


class SaleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleChannel
        fields = ['id', 'sale_channel', 'status', 'create_by', 'update_by']




class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'create_by', 'update_by', 'status']


class PriceToppingSerializer(serializers.ModelSerializer): 
    sale_channel = SaleChannelSerializer(read_only=True)
    sale_channel_id = serializers.IntegerField()
    topping_id = serializers.IntegerField()

    class Meta:
        model = PriceTopping
        fields = ['id', 'topping_id', 'sale_channel_id', 'price',
                  'sale_channel', 'create_by', 'update_by']


class ToppingSerializer(serializers.ModelSerializer):
    price_topping = PriceToppingSerializer(
        many=True, read_only=True, source="pricetopping")

    class Meta:
        model = Topping
        fields = ['id', 'status', 'name', 'price_topping',
                  'img', 'code', 'create_by', 'update_by']

class TableToppingSerializer(serializers.ModelSerializer):
    topping_id = serializers.IntegerField()
    type_topping_id = serializers.IntegerField()
    topping = ToppingSerializer(read_only=True)

    class Meta:
        model = TableTopping
        fields = ['id', 'topping_id', 'type_topping_id', 'create_by', 'update_by','topping']


class TypeToppingSerializer(serializers.ModelSerializer):
    tabletopping_set = TableToppingSerializer(many=True,read_only=True)
    class Meta:
        model = TypeTopping
        fields = ['id', 'type_topping','create_by','update_by','tabletopping_set']

class PriceProductSerializer(serializers.ModelSerializer):
    sale_channel = SaleChannelSerializer(read_only=True)
    sale_channel_id = serializers.IntegerField()

    class Meta:
        model = PriceProduct
        fields = ['id', 'product', 'sale_channel_id',
                  'sale_channel','price', 'create_by', 'update_by']


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    category = ProductCategorySerializer(read_only=True)
    type_topping = TypeToppingSerializer(read_only=True)
    type_topping_id = serializers.IntegerField()
    price = PriceProductSerializer(many=True,read_only=True, source='priceproduct_set')

    class Meta:
        model = Product
        fields = ['id', 'status', 'name', 'img', 'code', 'category', 'type_topping',
                  'category_id', 'type_topping_id', 'create_by', 'update_by', 'price']
