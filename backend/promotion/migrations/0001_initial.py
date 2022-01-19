<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-01-18 11:29
=======
# Generated by Django 3.0.7 on 2022-01-18 11:32
>>>>>>> 0ff6639c921e9b8d28fa538608247603083c3d0a

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import promotion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(max_length=100)),
                ('start_promotion_date', models.DateField()),
                ('end_promotion_date', models.DateField()),
                ('end_reward_redemption', models.DateField()),
                ('price_per_point', models.IntegerField()),
                ('point', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promotion_point_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion_point_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_voucher, verbose_name='Image')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_percent', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('qty', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='voucher_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='voucher_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
<<<<<<< HEAD
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_rewards, verbose_name='Image')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
>>>>>>> 0ff6639c921e9b8d28fa538608247603083c3d0a
                ('description', models.TextField(blank=True, null=True)),
                ('qty', models.IntegerField()),
                ('point', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
                ('status', models.BooleanField(default=True)),
                ('is_pre_order', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rewards_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rewards_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Redemption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField()),
                ('status_given', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_redemption, verbose_name='Image')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
                ('deal_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='redemption_deal_user', to=settings.AUTH_USER_MODEL)),
                ('deliver_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='redemption_deliver_user', to=settings.AUTH_USER_MODEL)),
                ('point_promotion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.pointpromotion')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.rewards')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_package, verbose_name='Image')),
                ('amount_day', models.IntegerField()),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.BooleanField(default=True)),
                ('total_amount', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promotion_package_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promotion_package_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.promotionpackage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.packageitem')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('signature', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_history, verbose_name='Image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exchange_history_create_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.rewards')),
                ('update_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exchange_history_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer')),
                ('point_promotion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='promotion.pointpromotion')),
            ],
        ),
        migrations.CreateModel(
            name='ConditionRewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('point_promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.pointpromotion')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.rewards')),
            ],
        ),
    ]
