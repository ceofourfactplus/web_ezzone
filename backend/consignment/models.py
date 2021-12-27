from django.db import models
from django.utils.translation import gettext_lazy as _
from backend.settings import AUTH_USER_MODEL
from raw_material.models import Unit


def upload_to_product(instance, filename):
    return 'consignment/{filename}'.format(filename=instance.name)


# class Consignment(models.Model):
#   nick_name = models.CharField(max_length=40)
#   first_name = models.CharField(max_length=40)
#   last_name = models.CharField(max_length=40)
#   line_id = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)
#   address = models.CharField(max_length=40)


class ConsignmentProduct(models.Model):
    NONE_PICK_UP = 0
    PRODUCT = 1
    MATERIAL = 2
    WAREHOUSE = (
        (NONE_PICK_UP, 'ไม่ต้องตัดสต็อก'),
        (PRODUCT, 'สินค้าพร้อมขาย'),
        (MATERIAL, 'วัตถุดิบ')
    )

    OUT_OF_STOCK = 0
    ALMOST_OUT_OF_STOCK = 1
    INSTOCK = 2
    STATUS_STOCK = (
        (OUT_OF_STOCK, 'สินค้าหมด'),
        (ALMOST_OUT_OF_STOCK, 'สินค้าเกือบหมด'),
        (INSTOCK, 'สินค้าพร้อมขาย')
    )

    NOT_USE_TOPPING = 0
    ROTI = 1
    DRINK = 2
    FOOD = 3
    TYPE_TOPPING = (
        (NOT_USE_TOPPING, 'ไม่มี toppping'),
        (ROTI, 'โรตี'),
        (DRINK, 'เครื่องดื่ม'),
        (FOOD, 'อาหาร')
    )

    SPICY = 1
    SWEET = 2
    FLAVOUR = (
        (SPICY, 'เผ็ด'),
        (SWEET, 'หวาน')
    )
    old_product = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, default=None)
    img = models.ImageField(
        _("Image"), upload_to=upload_to_product, default=None, null=True)
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    is_topping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    flavour_level = models.BooleanField(default=False)
    status = models.IntegerField(default=INSTOCK, choices=STATUS_STOCK)
    remain = models.IntegerField(default=0)
    flavour = models.IntegerField(choices=FLAVOUR)
    minimum = models.IntegerField(default=0)
    maximum = models.IntegerField(default=None, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    consignment = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, default=None)
    share = models.IntegerField(default=0)
    type_topping = models.IntegerField(choices=TYPE_TOPPING)
    warehouse = models.IntegerField(choices=WAREHOUSE, default=NONE_PICK_UP)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="consignment_product_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="consignment_product_update_by", 
        null=True, blank=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True, default=None)

