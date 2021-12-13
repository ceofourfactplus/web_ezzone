from django.contrib.auth import default_app_config
from django.contrib.auth.models import AbstractUser
from django.db import models
from backend.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _ 

def upload_to_user(instance,filename):
    return 'user/{filename}'.format(filename=instance.username)

class User(AbstractUser):
  is_owner = models.BooleanField(default=False)
  birth_day = models.BooleanField(blank=True,null=True)
  is_working = models.BooleanField(default=True)
  gender = models.CharField(max_length=30)
  img = models.ImageField(_("Image"), upload_to=upload_to_user,default='topping/default.png')

class Permission(models.Model):
  permission = models.CharField(max_length=50)
  customer = models.BooleanField(default=False)
  material = models.BooleanField(default=False)
  pos = models.BooleanField(default=False)
  product =  models.BooleanField(default=False)
  promotion = models.BooleanField(default=False)
  raw_material = models.BooleanField(default=False)
  user = models.BooleanField(default=False)

class UserPermission(models.Model):
  permission = models.ForeignKey(Permission,on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)

class Login(models.Model):
  token = models.CharField
  user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT)
  login_at = models.DateTimeField(auto_now_add=True)
  logout_at = models.DateTimeField(auto_now_add=True)
  time_login = models.TimeField()