from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to_customer(instance,filename):
    return 'customer/{filename}'.format(filename=str(instance.first_name)+'_'+str(instance.last_name))


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=50, null=True)
    address = models.TextField(default='')
    img = models.ImageField(_("Image"),null=True,upload_to=upload_to_customer)
    email = models.EmailField(null=True)


