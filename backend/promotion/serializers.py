from django.db.models import fields
from rest_framework import serializers
from user.serializers import UserSerializer

from .models import PointPromotion, Voucher, PromotionPackage, PackageItem, ItemTopping

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
      'amount',
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
  class Meta:
    model = PackageItem
    fields = [
      'id',
      'product_id',
      'amount',
      'total_price',
      'description',
      'package_id',
    ]
    
class ItemToppingSerializer(serializers.ModelSerializer):
  product_id = serializers.IntegerField()
  item_id = serializers.IntegerField()
  class Meta:
    model = ItemTopping
    fields = [
      'id',
      'topping_id',
      'amount',
      'total_price',
      'description',
      'item_id',
    ]