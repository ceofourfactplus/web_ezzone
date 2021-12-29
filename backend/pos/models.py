
from django.db import models
from promotion.models import PromotionPackage, Voucher, PointPromotion
from product.models import SaleChannel, Product,Topping
from backend.settings import AUTH_USER_MODEL
from customer.models import Customer
from consignment.models import ConsignmentProduct

from django.utils.translation import gettext_lazy as _


def upload_to_payment(instance, filename):
    return 'payment/{filename}'.format(filename=filename)


class Payment(models.Model):
    icon = models.ImageField(_("Image"), upload_to=upload_to_payment)
    payment = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    descriptions = models.TextField(null=True, blank=True)


class Order(models.Model):
    DELIVERY = '1'
    EATHERE = '0'
    STATUS_DELIVERY = (
        (DELIVERY, 'delivery'),
        (EATHERE, 'eat_here')
    )

    ON_COOKING = '1'
    ON_DELIVERY = '2'
    FINISH = '3'
    STATUS_ORDER = (
        (ON_COOKING, 'on cooking'),
        (ON_DELIVERY, 'on delivery'),
        (FINISH, 'finish'),
    )

    status_delivery = models.IntegerField(choices=STATUS_DELIVERY)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_amount = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    sale_channel = models.ForeignKey(SaleChannel, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    delivery_price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    status_order = models.IntegerField(
        choices=STATUS_ORDER, default=ON_COOKING)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="order_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="order_update_by", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    voucher = models.ForeignKey(
        Voucher, on_delete=models.PROTECT, null=True, blank=True)
    promotion = models.ForeignKey(
        PointPromotion, on_delete=models.PROTECT, null=True, blank=True)
    point = models.IntegerField(null=True,blank=True)
    old_order = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)


class OrderItem(models.Model):
    FLAVOUR_0 = '0'
    FLAVOUR_50 = '1'
    FLAVOUR_100 = '2'
    FLAVOUR_150 = '3'
    FLAVOUR_LEVEL = (
        (FLAVOUR_0, 'none'),
        (FLAVOUR_50, 'low'),
        (FLAVOUR_100, 'medium'),
        (FLAVOUR_150, 'very')
    )

    flavour_level = models.IntegerField(choices=FLAVOUR_LEVEL, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    topping = models.ForeignKey(Topping, on_delete=models.PROTECT, null=True)
    conignment = models.ForeignKey(ConsignmentProduct, on_delete=models.PROTECT, null=True)
    package = models.ForeignKey(
        PromotionPackage, on_delete=models.PROTECT, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True)
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(null=True)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    clear_consignment = models.BooleanField(default=False)
    old_item = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True)
    voucher = models.ForeignKey(
        Voucher, on_delete=models.PROTECT, null=True, blank=True)
    promotion = models.ForeignKey(
        PointPromotion, on_delete=models.PROTECT, null=True, blank=True)


class OrderItemTopping(models.Model):
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    topping = models.ForeignKey(Product, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True, blank=True)
    old_topping = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True)
