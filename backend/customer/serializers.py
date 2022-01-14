from django.db.models import fields
from customer.models import Customer, AddressCustomer
from rest_framework import serializers


class AddressCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressCustomer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    addresscustomer_set = AddressCustomerSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'nick_name', 'first_name',
                  'last_name', 'phone_number', 'gender',
                  'img', 'email', 'addresscustomer_set','birth_date',
                  'line_customer_id', 'invited_by', 'date_joined', 'last_joined']
