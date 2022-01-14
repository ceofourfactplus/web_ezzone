from django.db.models import fields
from rest_framework import serializers
from user.serializers import UserSerializer
from product.serializers import ProductSerializer, ProductCategorySerializer, PriceProductSerializer, ToppingCategorySerializer
from .models import PointPromotion, Voucher, PromotionPackage, PackageItem, ItemTopping, Rewards, ConditionRewards

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
    
class PromotionPackageSerializer(serializers.ModelSerializer):
  create_by_id = serializers.IntegerField()
  update_by_id = serializers.IntegerField()
  class Meta:
    model = PromotionPackage
    fields = [
      'id',
      'promotion',
      'start_date',
      'img',
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
    ]
    
class PackageItemSerializer(serializers.ModelSerializer):
  product_id = serializers.IntegerField()
  package_id = serializers.IntegerField()
  product_set = ProductSerializer(read_only=True, source='product')
  package_set = PromotionPackageSerializer(read_only=True, source='package')
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
      'package_set',
    ]
    
class ItemToppingSerializer(serializers.ModelSerializer):
  topping_id = serializers.IntegerField()
  item_id = serializers.IntegerField()
  topping_set = ProductSerializer(read_only=True, source='topping')
  item_set = PackageItemSerializer(read_only=True, source='item')
  class Meta:
    model = ItemTopping
    fields = [
      'id',
      'topping_id',
      'qty',
      'total_price',
      'description',
      'item_id',
      'item_set',
      'topping_set',
    ]
    
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