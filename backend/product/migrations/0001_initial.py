# Generated by Django 3.0.7 on 2021-12-12 11:17

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#ffffff', max_length=18)),
                ('status', models.BooleanField(default=True)),
                ('img', models.ImageField(upload_to=product.models.upload_to_sale_channel, verbose_name='Image')),
                ('sale_channel', models.CharField(max_length=100)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sale_channel_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sale_channel_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('type_category', models.IntegerField(choices=[(1, 'ของหวาน'), (2, 'เครื่องดื่ม'), (3, 'อาหาร')])),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_category_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_category_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=product.models.upload_to_product, verbose_name='Image')),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('is_topping', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('flavour_level', models.BooleanField()),
                ('status', models.BooleanField(default=True)),
                ('remain', models.IntegerField()),
                ('flavour', models.IntegerField(choices=[(1, 'เผ็ด'), (2, 'หวาน')])),
                ('minimum', models.IntegerField(default=1)),
                ('percent', models.IntegerField(blank=True, null=True)),
                ('type_topping', models.IntegerField(choices=[(1, 'โรตี'), (2, 'เครื่องดื่ม'), (3, 'อาหาร')])),
                ('warehouse', models.IntegerField(choices=[(0, 'ไม่ต้องตัดสต็อก'), (1, 'สินค้าพร้อมขาย'), (2, 'วัตถุดิบ')])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductCategory')),
                ('consignment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_create_by', to=settings.AUTH_USER_MODEL)),
                ('old_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Product')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='price_product_create_by', to=settings.AUTH_USER_MODEL)),
                ('old_price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.PriceProduct')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('sale_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SaleChannel')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='price_product_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='add_product_create_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_product_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
