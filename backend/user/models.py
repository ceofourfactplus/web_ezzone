from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _ 

def upload_to_user(instance,filename):
    return 'user/{filename}'.format(filename=instance.username)

class User(AbstractUser):
  is_chef = models.BooleanField(default=False)
  is_bartender = models.BooleanField(default=False)
  is_purchaser = models.BooleanField(default=False)
  is_service = models.BooleanField(default=False)
  born_at = models.BooleanField(blank=True,null=True)
  img = models.ImageField(_("Image"), upload_to=upload_to_user,default='topping/default.png')