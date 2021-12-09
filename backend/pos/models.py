
from django.db import models
from product.models import SaleChannel, Product, Topping
from backend.settings import AUTH_USER_MODEL

def upload_to_customer(instance,filename):
    return 'customer/{folder}/{filename}'.format(folder=instance.folder,filename=filename)


def upload_to_payment(instance, filename):
    return 'payment/{filename}'.format(filename=filename)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=50, null=True)
    address = models.TextField(default='')
    img = models.ImageField(null=True,upload_to=upload_to_customer)
    folder = models.CharField(null=True,max_length=1000)


class Payment(models.Model):
    icon = models.ImageField(upload_to=upload_to_payment)
    payment = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    descriptions = models.TextField(default='')
    
class Promotion(models.Model):
    promotion = models.CharField(max_length=255)
    descriptions = models.TextField
    discount = models.IntegerField


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
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    sale_channel = models.ForeignKey(SaleChannel, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    descriptions = models.TextField(default='')
    status_order = models.IntegerField(
        choices=STATUS_ORDER, default=ON_COOKING)
    create_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="order_create_by")
    update_by = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="order_update_by")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)


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

    flavour_level = models.IntegerField(choices=FLAVOUR_LEVEL)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField(null=True)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



class OrderItemTopping(models.Model):
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.PROTECT)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField(null=True)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

