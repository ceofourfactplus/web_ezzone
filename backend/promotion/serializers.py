from django.db.models import fields
from rest_framework import serializers
from user.serializers import UserSerializer
from product.serializers import ProductSerializer, ProductCategorySerializer, PriceProductSerializer, ToppingCategorySerializer, OnlyPriceProduct, ToppingSerializer
from customer.serializers import CustomerSerializer, AddressCustomerSerializer
from .models import PointPromotion, Voucher, PromotionPackage, PackageItem, ItemTopping, Rewards, ConditionRewards, Redemption, CustomerPoint, ExchangeHistory
from pprint import pprint

class PointListSerializer(serializers.ModelSerializer):
  class Meta:
    model = PointPromotion
    fields = '__all__'
    
class VoucherListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Voucher
    fields = '__all__'
class PackageListSerializer(serializers.ModelSerializer):
  class Meta:
    model = PromotionPackage
    fields = '__all__'
    
class PromotionPackageImage(serializers.ModelSerializer):
    class Meta:
        model = PromotionPackage
        fields = ['img']

class PointSerializer(serializers.ModelSerializer):
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  create_by_set = UserSerializer(read_only=True, source="user")
  update_by_set = UserSerializer(read_only=True, source="user")
  class Meta:
    model = PointPromotion
    fields = [
      'id',
      'promotion',
      'start_promotion_date',
      'end_promotion_date',
      'end_reward_redemption',
      'price_per_point',
      'point',
      'status',
      'description',
      'create_by_id',
      'update_by_id',
      'create_by_set',
      'update_by_set',
      'create_at',
      'update_at',
    ]
    
class VoucherSerializer(serializers.ModelSerializer):
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  class Meta:
    model = Voucher
    fields = [
      'id',
      'voucher',
      'code',
      'img',
      'discount',
      'start_date',
      'end_date',
      'is_percent',
      'description',
      'qty',
      'status',
      'create_by_id',
      'update_by_id',
      'create_at',
      'update_at',
    ]
    
    
class ItemToppingSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required=False)
  topping_id = serializers.IntegerField()
  item_id = serializers.IntegerField(read_only=True)
  topping_set = ToppingSerializer(read_only=True, source='topping')
  description = serializers.CharField(required=False, allow_blank=True)
  class Meta:
    model = ItemTopping
    fields = [
      'id',
      'topping_id',
      'qty',
      'total_price',
      'description',
      'item_id',
      'topping_set',
    ]
      
class PackageItemSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required=False)
  product_id = serializers.IntegerField()
  package_id = serializers.IntegerField(read_only=True)
  product_set = ProductSerializer(read_only=True, source='product')
  itemtopping_set = ItemToppingSerializer(many=True)
  description = serializers.CharField(required=False, allow_blank=True)
  class Meta:
    model = PackageItem
    fields = [
      'id',
      'product_id',
      'qty',
      'total_price',
      'description',
      'package_id',
      'product_set',
      'itemtopping_set',
    ] 
    

class PromotionPackageSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required=False)
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  description = serializers.CharField(required=False, allow_blank=True)
  packageitem_set = PackageItemSerializer(many=True)
  img = serializers.ImageField(read_only=True)

  class Meta:
    model = PromotionPackage
    fields = [
      'id',
      'start_date',
      'promotion',
      'amount_day',
      'discount_price',
      'normal_price',
      'status',
      'total_amount',
      'description',
      'create_by_id',
      'update_by_id',
      'create_at',
      'update_at',
      'packageitem_set',
      'img'
    ]
    
  def create(self, validated_data):
    print(validated_data)
    packageitem_set = validated_data.pop('packageitem_set')
    pp = PromotionPackage.objects.create(**validated_data)
    if packageitem_set != []:
      for item in packageitem_set:
        itemtopping_set = item.pop('itemtopping_set')
        package_item = PackageItem.objects.create(**item, package=pp)
        if not itemtopping_set == []:
            for topping in itemtopping_set:
                ItemTopping.objects.create(**topping, item=package_item)
    return pp
          

class RewardsSerializer(serializers.ModelSerializer):
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  class Meta:
    model = Rewards
    fields = [
      'id',
      'reward',
      'img',
      'value',
      'description',
      'qty',
      'point',
      'cost',
      'status',
      'is_pre_order',
      'create_by_id',
      'update_by_id',
      'create_at',
      'update_at',
    ]
    
class ConditionRewardsSerializer(serializers.ModelSerializer):
  point_promotion_id = serializers.IntegerField()
  reward_id = serializers.IntegerField()
  point_promotion_set = PointSerializer(read_only=True, source='point_promotion')
  reward_set = RewardsSerializer(read_only=True, source='reward')
  class Meta:
    model = ConditionRewards
    fields = [
      'id',
      'point_promotion_id',
      'reward_id',
      'point_promotion_set',
      'reward_set',
      'point',
    ]
    
class RedemptionSerializer(serializers.ModelSerializer):
  customer_id = serializers.IntegerField()
  reward_id = serializers.IntegerField()
  deal_user_id = serializers.IntegerField()
  deliver_user_id = serializers.IntegerField()
  point_promotion_id = serializers.IntegerField()
  point_promotion_set = PointSerializer(read_only=True, source='point_promotion')
  reward_set = RewardsSerializer(read_only=True, source='reward')
  deal_user_set = UserSerializer(read_only=True, source="user")
  deliver_user_set = UserSerializer(read_only=True, source="user")
  customer_set = CustomerSerializer(read_only=True, source="user")
  
  class Meta:
    model = Redemption
    fields = [
      'id',
      'customer_id',
      'reward_id',
      'deal_user_id',
      'deliver_user_id',
      'point_promotion_id',
      'status_given',
      'point',
      'due_date',
      'description',
      'create_at',
      'img',
      'point_promotion_set',
      'reward_set',
    ]
    
class CustomerPointSerializer(serializers.ModelSerializer):
  customer_id = serializers.IntegerField()
  point_promotion_id = serializers.IntegerField()
  customer_set = CustomerSerializer(read_only=True, source="customer")
  point_promotion_set = PointSerializer(read_only=True, source='point_promotion')
  
  class Meta:
    model = CustomerPoint
    fields = [
      'id',
      'point',
      'description',
      'customer_id',
      'point_promotion_id',
      'customer_set',
      'point_promotion_set',
    ]
    
class ExchangeHistorySerializer(serializers.ModelSerializer):
  customer_id = serializers.IntegerField()
  reward_id = serializers.IntegerField()
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  create_by_set = UserSerializer(read_only=True, source="user")
  customer_set = CustomerSerializer(read_only=True, source="customer")
  reward_set = RewardsSerializer(read_only=True, source='reward')
  
  class Meta:
    model = ExchangeHistory
    fields = [
      'id',
      'point',
      'qty',
      'signature',
      'customer_id',
      'reward_id',
      'customer_set',
      'reward_set',
      'create_by_set',
      'create_at',
      'create_by_id',
      'update_by_id',
    ]