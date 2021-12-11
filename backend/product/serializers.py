from rest_framework import serializers
from product.models import ProductCategory, SaleChannel, Product, PriceProduct


class SaleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleChannel
        fields = ['id', 'sale_channel', 'color',
                  'status', 'create_by', 'update_by', 'img']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'color',
                  'create_by', 'update_by', 'status']




class PriceProductSerializer(serializers.ModelSerializer):
    sale_channel = SaleChannelSerializer(read_only=True)
    sale_channel_id = serializers.IntegerField()

    class Meta:
        model = PriceProduct
        fields = ['id', 'product', 'sale_channel_id',
                  'sale_channel', 'price', 'create_by', 'update_by']


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    category = ProductCategorySerializer(read_only=True)
    type_topping_id = serializers.IntegerField()
    price = PriceProductSerializer(
        many=True, read_only=True, source='priceproduct_set')

    class Meta:
        model = Product
        fields = ['id', 'status', 'name', 'img', 'code', 'category', 'type_topping',
                  'category_id', 'type_topping_id', 'create_by', 'update_by', 'price', 'flavour']
