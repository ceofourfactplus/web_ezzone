from promotions.serializers import PromotionSerializer
from .models import Customer,CustomerStamp
from rest_framework import serializers

class CustomerStampSerializer(serializers.ModelSerializer):
  promotion_set = PromotionSerializer(read_only=True)
  promotion_id = serializers.IntegerField
  customer_id = serializers.IntegerField
  class Meta:
    model = CustomerStamp
    fields = ['customer_id','promotion_id','promotion_set','point','description']

class CustomeSerializer(serializers.ModelSerializer):
  customer_stamp_list = CustomerStampSerializer(read_only=True,many=True)
 
  class Meta:
    model = Customer
    fields = ['frist_name','last_name','phone_number','gender',
              'address','img','email','customer_stamp_list']
