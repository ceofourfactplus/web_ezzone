from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to_customer(instance,filename):
    return 'customer/{filename}'.format(filename=str(instance.first_name)+'_'+str(instance.last_name))


class Customer(models.Model):
    nick_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField()
    img = models.ImageField(_("Image"),upload_to=upload_to_customer,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    line_id = models.CharField(max_length=100,null=True,blank=True)
    invited_by = models.ForeignKey('self',on_delete=models.PROTECT,null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now_add=True)
    
# class LevelCustomer(models.Model):
#     level = models.CharField
#     price = models.DecimalField
#     time = models.TextField

