# Generated by Django 3.0.7 on 2022-01-14 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('promotion', '0001_initial'),
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20220114_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='voucher_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='voucher',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='voucher_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rewards',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rewards_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rewards',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rewards_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='redemption',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='redemption',
            name='deal_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='redemption_deal_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='redemption',
            name='deliver_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='redemption_deliver_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='redemption',
            name='point_promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.PointPromotion'),
        ),
        migrations.AddField(
            model_name='redemption',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.Rewards'),
        ),
        migrations.AddField(
            model_name='promotionpackage',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promotion_package_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='promotionpackage',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion_package_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pointpromotion',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promotion_point_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pointpromotion',
            name='update_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion_point_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='packageitem',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.PromotionPackage'),
        ),
        migrations.AddField(
            model_name='packageitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product'),
        ),
        migrations.AddField(
            model_name='itemtopping',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.PackageItem'),
        ),
        migrations.AddField(
            model_name='itemtopping',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product'),
        ),
        migrations.AddField(
            model_name='customerpoint',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='customerpoint',
            name='point_promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.PointPromotion'),
        ),
        migrations.AddField(
            model_name='conditionrewards',
            name='point_promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.PointPromotion'),
        ),
        migrations.AddField(
            model_name='conditionrewards',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.Rewards'),
        ),
    ]
