from rest_framework import serializers
from product.models import ProductCategory, SaleChannel, Product, PriceProduct, SetTopping,ToppingCategory,Topping,PriceTopping
from raw_material.serializers import UnitSerializer
from user.serializers import UserSerializer


class SaleChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleChannel
        fields = ['id', 'sale_channel', 'gp',
                  'status', 'create_by', 'update_by', 'img',
                  'create_at', 'update_at']


class ToppingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToppingCategory
        fields = ['id', 'category',
                  'create_by', 'update_by',]


class PriceToppingSerializer(serializers.ModelSerializer):
    sale_channel_id = serializers.IntegerField()
    topping_id = serializers.IntegerField()

    class Meta:
        model = PriceTopping
        fields = ['id', 'topping_id', 'sale_channel_id','price']

class SetToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetTopping
        fields = ['id','topping','category']

class ToppingSerializer(serializers.ModelSerializer):

    # all id
    unit_id = serializers.IntegerField()
    old_product_id = serializers.IntegerField(allow_null=True, required=False)
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField(allow_null=True, required=False)

    # all set
    unit_set = UnitSerializer(read_only=True, source='unit')
    old_product_set = serializers.IntegerField()
    create_by_set = UserSerializer(read_only=True, source='create_by')
    update_by_set = UserSerializer(read_only=True, source='update_by')

    class Meta:
        model = Topping
        fields = [
            'id', 'img', 'code', 'name', 'is_active', 'status',
            'remain', 'flavour', 'minimum', 'maximum', 'warehouse', 'create_at',
            'update_at',
            # all set
            'unit_set', 'create_by_set',
            'update_by_set','old_product_set',

            # all id
            'old_product_id',
            'unit_id', 'create_by_id',
            'update_by_id',
        ]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'type_category',
                  'create_by', 'update_by']


class PriceProductSerializer(serializers.ModelSerializer):
    sale_channel_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

    class Meta:
        model = PriceProduct
        fields = ['id', 'status', 'product_id', 'sale_channel_id',
                  'price', 'create_by',
                  'update_by', 'create_at', 'update_at'
                  ]


class ProductSerializer(serializers.ModelSerializer):

    # all id
    category_id = serializers.IntegerField()
    unit_id = serializers.IntegerField()
    old_product_id = serializers.IntegerField(allow_null=True, required=False)
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField(allow_null=True, required=False)

    # all set
    category_set = ProductCategorySerializer(read_only=True, source='category')
    unit_set = UnitSerializer(read_only=True, source='unit')
    priceproduct_set = PriceProductSerializer(many=True, read_only=True)
    # old_product_set = serializers.IntegerField()
    create_by_set = UserSerializer(read_only=True, source='create_by')
    update_by_set = UserSerializer(read_only=True, source='update_by')

    class Meta:
        model = Product
        fields = [
            'id', 'img', 'code', 'name',
            'is_active', 'flavour_level', 'status',
            'remain', 'flavour', 'minimum', 'maximum',
            'type_topping', 'warehouse', 'create_at',
            'update_at', 'priceproduct_set',

            # all set
            'unit_set', 'category_set', 'create_by_set',
            'update_by_set',

            # all id
            'old_product_id',
            'unit_id', 'category_id', 'create_by_id',
            'update_by_id',
        ]
