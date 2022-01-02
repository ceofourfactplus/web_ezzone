import datetime
from rest_framework import serializers
from product.models import ProductCategory, SaleChannel, Product, PriceProduct, SetTopping, ToppingCategory, Topping, PriceTopping
from raw_material.serializers import UnitSerializer
from user.serializers import UserSerializer
from pprint import pprint


class PriceToppingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PriceTopping
        fields = ["id", "price", "topping", "sale_channel", "status"]
        read_only_fields = ('sale_channel',)


class PriceProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PriceProduct
        fields = ["id", "price", "product", "sale_channel", "status"]
        read_only_fields = ('sale_channel',)

class ToppingSerializer(serializers.ModelSerializer):

    # all id
    unit_id = serializers.IntegerField()
    old_product_id = serializers.IntegerField(allow_null=True, required=False)
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField(allow_null=True, required=False)
    pricetopping_set = PriceToppingSerializer(read_only=True, many=True)
    # all set
    unit_set = UnitSerializer(read_only=True, source='unit')
    old_product_set = serializers.IntegerField(allow_null=True, required=False)
    create_by_set = UserSerializer(read_only=True, source='create_by')
    update_by_set = UserSerializer(read_only=True, source='update_by')

    class Meta:
        model = Topping
        fields = [
            'id', 'img', 'code', 'name', 'is_active', 'status',
            'remain', 'minimum', 'pricetopping_set', 'maximum', 'type_topping', 'warehouse', 'create_at',
            # all set
            'unit_set', 'create_by_set',
            'update_by_set', 'old_product_set',

            # all id
            'old_product_id',
            'unit_id', 'create_by_id',
            'update_by_id',
        ]


class SetToppingSerializer(serializers.ModelSerializer):
    topping_set = ToppingSerializer(read_only=True,source="topping") 

    class Meta:
        model = SetTopping
        fields = ['category','topping','topping_set']


class ToppingCategorySerializer(serializers.ModelSerializer):
    settopping_set = SetToppingSerializer(read_only=True, many=True)

    class Meta:
        model = ToppingCategory
        fields = ['id', 'category',
                  'create_by', 'update_by', 'settopping_set']


class SaleChannelSerializer(serializers.ModelSerializer):
    price_topping = PriceToppingSerializer(many=True, source="pricetopping")
    price_product = PriceProductSerializer(many=True, source="priceproduct")
    id = serializers.IntegerField(required=False)

    class Meta:
        model = SaleChannel
        fields = ['id', 'sale_channel', 'gp',
                  'status', 'create_by', 'update_by', 'img',
                  'create_at', 'update_at', 'price_topping', 'price_product']

    def create(self, validated_data):
        price_toppings = validated_data.pop('pricetopping')
        price_products = validated_data.pop('priceproduct')
        sale_channel = SaleChannel.objects.create(**validated_data)

        for price_topping in price_toppings:
            PriceTopping.objects.create(
                **price_topping, sale_channel=sale_channel)

        for price_product in price_products:
            PriceProduct.objects.create(
                **price_product, sale_channel=sale_channel)
        return sale_channel

    def update(self, instance, validated_data):

        priceproduct_id = [c['id'] for c in validated_data['priceproduct'] if c.get('id')]
        PriceProduct.objects.filter(sale_channel_id=instance.id).exclude(id__in=priceproduct_id).delete()

        to_be_create = [c for c in validated_data['priceproduct'] if c.get('id') == None]
        for p in to_be_create: PriceProduct.objects.create(**p, sale_channel_id=instance.id)

        to_be_update = [c for c in validated_data['priceproduct'] if c.get('id')]
        for p in to_be_update: PriceProduct.objects.filter(id=p['id']).update(**p)

        return instance
        # price_toppings = validated_data.pop('pricetopping')
        # price_products = validated_data.pop('priceproduct')
        # print(price_products)
        # instance.sale_channel = validated_data.get("sale_channel",instance.sale_channel)
        # instance.gp = validated_data.get("gp",instance.gp)
        # instance.status = validated_data.get("status",instance.status)
        # instance.update_by = validated_data.get("update_by",instance.update_by)
        # # instance.update_at = datetime.datetime.now()
        # instance.save()
        # keep_topping = []
        # keep_product = []
        # for price_topping in price_toppings:
        #     if "id" in price_topping.keys():
        #         print('in loop')
        #         if PriceTopping.objects.filter(id=price_topping["id"]).exists():
        #             c = PriceTopping.objects.get(id=price_topping["id"])
        #             c.price = price_topping.get('price',c.price)
        #             c.topping = price_topping.get('topping',c.topping)
        #             c.save()
        #             keep_topping.append(c.id)
        #         else:
        #             continue
        #     else:
        #         c = PriceTopping.objects.create(**price_topping,sale_channel=instance)

        # print(instance.pricetopping)
        # print(instance.priceproduct)
        # for price_topping in instance.pricetopping:
        #     if price_topping not in keep_topping:
        #         price_topping.delete()

        # for price_product in price_products:
        #     print(price_product.keys())
        #     if "id" in price_product.keys():

        #         print(price_product["id"])

        #         if PriceProduct.objects.filter(id=price_product["id"]).exists():
        #             print('check price')
        #             c = PriceProduct.objects.get(id=price_product["id"])
        #             c.price = price_product.get('price',c.price)
        #             c.product = price_product.get('product',c.product)
        #             c.save()
        #             keep_product.append(c.id)
        #         else:
        #             continue
        #     else:
        #         c = PriceProduct.objects.create(**price_product,sale_channel=instance)
        # for price_product in instance.priceproduct:
        #     if price_product.id not in keep_product:
        #         print('delete')
        #         price_product.delete()

        # return instance



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category', 'type_category',
                  'create_by', 'update_by']


class ProductSerializer(serializers.ModelSerializer):

    # all id
    category_id = serializers.IntegerField()
    unit_id = serializers.IntegerField()
    old_product_id = serializers.IntegerField(allow_null=True, required=False)
    create_by_id = serializers.IntegerField()
    update_by_id = serializers.IntegerField(allow_null=True, required=False)
    topping_category_id = serializers.IntegerField(
        allow_null=True, required=False)
    # all set
    category_set = ProductCategorySerializer(read_only=True, source='category')
    unit_set = UnitSerializer(read_only=True, source='unit')
    priceproduct_set = PriceProductSerializer(many=True, read_only=True)
    # old_product_set = serializers.IntegerField()
    topping_category_set = ToppingCategorySerializer(read_only=True,source="topping_category")
    create_by_set = UserSerializer(read_only=True, source='create_by')
    update_by_set = UserSerializer(read_only=True, source='update_by')

    class Meta:
        model = Product
        fields = [
            'id', 'img', 'code', 'name',
            'is_active', 'flavour_level', 'status',
            'remain', 'flavour', 'minimum', 'maximum',
            'topping_category_id', 'warehouse', 'create_at',
            'update_at', 'priceproduct_set',

            # all set
            'unit_set', 'category_set', 'create_by_set',
            'update_by_set', 'topping_category_set',

            # all id
            'old_product_id',
            'unit_id', 'category_id', 'create_by_id',
            'update_by_id',
        ]
