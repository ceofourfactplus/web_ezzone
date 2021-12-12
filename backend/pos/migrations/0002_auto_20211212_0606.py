# Generated by Django 3.0.7 on 2021-12-12 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('pos', '0001_initial'),
        ('promotion', '0002_auto_20211212_0606'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20211212_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemtopping',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='old_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pos.OrderItem'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='promotion.PromotionPackage'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='old_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pos.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='promotion.PointPromotion'),
        ),
        migrations.AddField(
            model_name='order',
            name='sale_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.SaleChannel'),
        ),
        migrations.AddField(
            model_name='order',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='promotion.Voucher'),
        ),
    ]
