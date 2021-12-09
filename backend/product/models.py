from django.db import models
from backend.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _ 
from colorfield.fields import ColorField

def upload_to_product(instance,filename):
    return 'product/{filename}'.format(filename=filename)

def upload_to_topping(instance,filename):
    return 'topping/{filename}'.format(filename=filename)

def upload_to_sale_channel(instance,filename):
    return 'sale_channel/{filename}'.format(filename=filename)

class ProductCategory(models.Model):
    color = ColorField(default='#ffffff')
    status = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_category_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_category_update_by")
    
class SaleChannel(models.Model):
    color = ColorField(format='hexa')
    status = models.BooleanField(default=True)
    img = models.ImageField(_("Image"), upload_to=upload_to_sale_channel)
    sale_channel = models.CharField(max_length=100)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sale_channel_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sale_channel_update_by")


class Topping(models.Model):

    code = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    img = models.ImageField(_("Image"), upload_to=upload_to_topping ,default='topping/default.png')
    name = models.CharField(max_length=50)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="topping_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="topping_update_by")


class TypeTopping(models.Model):
    type_topping = models.CharField(max_length=100)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="type_topping_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="type_topping_update_by")


class PriceTopping(models.Model):
    status = models.BooleanField(default=True)
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_topping_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_topping_update_by")


class TableTopping(models.Model):
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)
    type_topping = models.ForeignKey(TypeTopping,on_delete=models.CASCADE)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="table_topping_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="table_topping_update_by")


class Product(models.Model):
    flavour = models.CharField(max_length=50)
    img = models.ImageField(_("Image"), upload_to=upload_to_product ,default='product/default.jpg')
    status = models.BooleanField(default=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    type_topping = models.ForeignKey(TypeTopping,on_delete=models.PROTECT)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_update_by")
    # is_edit = models.BooleanField
    # edit_for =  models.PrimeryKeyField()


class PriceProduct(models.Model):
    status = models.BooleanField(default=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # old_price
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_product_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_product_update_by")
