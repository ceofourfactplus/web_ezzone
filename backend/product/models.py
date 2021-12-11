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
    DESSERT = 1
    DRINK = 2
    FOOD = 3 
    TYPE_CATEGORY=(
        (DESSERT,'ของหวาน'),
        (DRINK,'เครื่องดื่ม'),
        (FOOD,'อาหาร')
    )
    status = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    type_category = models.IntegerField(choices=TYPE_CATEGORY)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_category_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_category_update_by")
    
class SaleChannel(models.Model):
    color = ColorField(default='#ffffff')
    status = models.BooleanField(default=True)
    img = models.ImageField(_("Image"), upload_to=upload_to_sale_channel)
    sale_channel = models.CharField(max_length=100)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sale_channel_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="sale_channel_update_by")

class Product(models.Model):
    NONE_PICK_UP = 0
    PRODUCT = 1
    MATERIAL = 2
    WAREHOUSE = (
        (NONE_PICK_UP,'ไม่ต้องตัดสต็อก'),
        (PRODUCT,'สินค้าพร้อมขาย'),
        (MATERIAL,'วัตถุดิบ') 
    )

    ROTI = 1
    DRINK = 2
    FOOD = 3 
    TYPE_TOPPING=(
        (ROTI,'โรตี'),
        (DRINK,'เครื่องดื่ม'),
        (FOOD,'อาหาร')
    )

    SPICY = 1
    SWEET = 2
    FLAVOUR = (
        (SPICY,'เผ็ด'),
        (SWEET,'หวาน')
    )

    old_product =  models.ForeignKey("self",on_delete=models.PROTECT,null=True)
    img = models.ImageField(_("Image"), upload_to=upload_to_product)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    is_topping = models.BooleanField()
    is_edit = models.BooleanField()
    is_active = models.BooleanField()
    flavour_level = models.BooleanField()
    status = models.BooleanField(default=True)
    remain = models.IntegerField()
    flavour = models.IntegerField(choices=FLAVOUR)
    minimum = models.IntegerField()
    type_topping = models.IntegerField(choices=TYPE_TOPPING)
    warehouse = models.IntegerField(choices=WAREHOUSE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="product_update_by")


class PriceProduct(models.Model):
    status = models.BooleanField(default=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sale_channel = models.ForeignKey(SaleChannel,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    old_price = models.AutoField(primary_key=True)
    is_edit = models.BooleanField
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_product_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="price_product_update_by")