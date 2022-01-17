# Generated by Django 3.0.7 on 2022-01-17 14:58

from django.db import migrations, models
import promotion.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionRewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('signature', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_history, verbose_name='Image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PointPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            ],
        ),
        migrations.CreateModel(
            name='PromotionPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_package, verbose_name='Image')),
                ('amount_day', models.IntegerField()),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('status', models.BooleanField(default=True)),
                ('total_amount', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Redemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField()),
                ('status_given', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_redemption, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to=promotion.models.upload_to_rewards, verbose_name='Image')),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField(blank=True, null=True)),
                ('qty', models.IntegerField()),
                ('point', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
                ('status', models.BooleanField(default=True)),
                ('is_pre_order', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            ],
        ),
    ]
