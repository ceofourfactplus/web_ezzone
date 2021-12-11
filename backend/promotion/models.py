from django.db import models
from django.utils.translation import gettext_lazy as _
from customer.models import Customer 
from backend.settings import AUTH_USER_MODEL
from product.models import Product

def upload_to_promotion(instance,filename):
    return 'promotion/{filename}'.format(filename=filename)

def upload_to_rewards(instance,filename):
    return 'rewards/{filename}'.format(filename=filename)

def upload_to_voucher(instance,filename):
    return 'voucher/{filename}'.format(filename=filename)

def upload_to_redemption(instance,filename):
    return 'redemption/{filename}'.format(filename=filename)

class PointPromotion(models.Model):
  promotion = models.CharField(max_length=255)
  start_promotion_date = models.DateField()
  end_promotion_date = models.DateField()
  end_reward_redemption = models.DateField()
  point_price = models.IntegerField()
  point = models.IntegerField()
  img = models.ImageField(_("Image"), upload_to=upload_to_promotion)
  status = models.BooleanField()
  description = models.TextField(null=True)
  create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="promotion_point_create_by")
  update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="promotion_point_update_by",null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True,null=True)
    

class Rewards (models.Model):
  reward = models.CharField(max_length=255)
  img = models.ImageField(_("Image"), upload_to=upload_to_rewards)
  value = models.DecimalField(max_digits=4,decimal_places=2)
  description = models.TextField(null=True)
  amount = models.IntegerField()
  create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="rewards_create_by")
  update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="rewards_update_by",null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True,null=True)
    

class ConditionRewards(models.Model):
  point_promotion = models.ForeignKey(PointPromotion,on_delete=models.CASCADE)
  rewards  = models.ForeignKey(Rewards,on_delete=models.CASCADE)
  point = models.IntegerField()


class Voucher (models.Model):
  voucher = models.CharField
  img = models.ImageField(_("Image"), upload_to=upload_to_voucher,)
  discount = models.DecimalField
  start_date = models.DateField
  end_date = models.DateField
  is_percent = models.BooleanField
  description = models.TextField(null=True)
  amount = models.IntegerField
  create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="voucher_create_by")
  update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="voucher_update_by",null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True,null=True)
    

class Redemption(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
  rewards = models.ForeignKey(Rewards,on_delete=models.PROTECT)
  deal_user =  models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT, related_name="redemption_deal_user")
  deliver_user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT, related_name="redemption_deliver_user")
  point_promotion = models.ForeignKey(PointPromotion,on_delete=models.PROTECT)
  create_at = models.DateTimeField(auto_now_add=True)
  point =  models.IntegerField()
  status_given = models.BooleanField(default=False)
  due_date = models.DateTimeField(null=True)
  description = models.TextField(null=True)
  img = models.ImageField(_("Image"), upload_to=upload_to_redemption ,null=True)

class PromotionPackage(models.Model):
  promotion = models.CharField(max_length=100)
  discount_price = models.DecimalField(max_digits=4,decimal_places=2)
  normal_price = models.DecimalField(max_digits=4,decimal_places=2)
  status_use = models.BooleanField(default=True)
  total_amount = models.IntegerField()
  description = models.TextField(null=True)

class PackageItem(models.Model):
  product = models.ForeignKey(Product,on_delete=models.PROTECT)
  amount = models.IntegerField()
  total_price = models.DecimalField(max_digits=4,decimal_places=2)
  description = models.TextField(null=True)
  package = models.ForeignKey(PromotionPackage,on_delete=models.CASCADE)

class ItemTopping(models.Model):
  topping = models.ForeignKey(Product,on_delete=models.PROTECT)
  item = models.ForeignKey(PromotionPackage,on_delete=models.CASCADE)
  amount = models.IntegerField()
  total_price = models.DecimalField(max_digits=3,decimal_places=2)
  description = models.TextField(null=True)


class CustomerPoint(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    point_promotion = models.ForeignKey(PointPromotion,on_delete=models.PROTECT)
    point = models.IntegerField()
    description = models.TextField()
