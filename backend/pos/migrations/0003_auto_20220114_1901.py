# Generated by Django 3.0.7 on 2022-01-14 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('promotion', '0001_initial'),
        ('customer', '0001_initial'),
        ('pos', '0002_auto_20220114_1901'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='package',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='promotion.PromotionPackage'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='topping',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Topping'),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.AddressCustomer'),
        ),
    ]
