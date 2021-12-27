from rest_framework import serializers
from product.models import ProductCategory, SaleChannel, Product, PriceProduct
from raw_material.serializers import UnitSerializer
from user.serializers import UserSerializer

class SaleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleChannel
        fields = ['id', 'sale_channel','gp',
                  'status', 'create_by', 'update_by', 'img']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'type_category',
                  'create_by', 'update_by', 'status']


class PriceProductSerializer(serializers.ModelSerializer):
    sale_channel = SaleChannelSerializer(read_only=True)
    sale_channel_id = serializers.IntegerField()

    class Meta:
        model = PriceProduct
        fields = ['id', 'product', 'sale_channel_id',
                  'sale_channel', 'price', 'create_by', 
                  'update_by']


class ProductSerializer(serializers.ModelSerializer):

    # all id
    category_id = serializers.IntegerField()
    unit_id = serializers.IntegerField()
    old_product_id = serializers.IntegerField(allow_null=True,required=False)
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField(allow_null=True,required=False)

    # all set
    category_set = ProductCategorySerializer(read_only=True,source='category')
    unit_set = UnitSerializer(read_only=True,source='unit')
    # old_product_set = serializers.IntegerField()
    consignment_set = UserSerializer(read_only=True,source='consignment')
    create_by_set = UserSerializer(read_only=True,source='create_by')
    update_by_set = UserSerializer(read_only=True,source='update_by')


    class Meta:
        model = Product
        fields = [
            'id', 'img', 'code', 'name', 'is_topping', 
            'is_active', 'flavour_level', 'status', 
            'remain', 'flavour', 'minimum', 'maximum', 
            'share', 'type_topping', 'warehouse', 'create_at',
            'update_at',

            # all set
            'old_product_id', 
            'unit_set', 'category_set', 'create_by_set', 
            'update_by_set',

            # all id
            # 'old_product_id', 
            'unit_id', 'category_id', 'create_by_id', 
            'update_by_id',
            ]
