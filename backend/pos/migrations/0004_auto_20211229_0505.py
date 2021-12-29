# Generated by Django 3.0.7 on 2021-12-29 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('promotion', '0001_initial'),
        ('pos', '0003_auto_20211229_0505'),
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
