# Generated by Django 3.0.7 on 2022-01-18 08:35

from django.db import migrations, models
import django.db.models.deletion
import pos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='1', max_length=20)),
                ('total_balance', models.DecimalField(decimal_places=2, max_digits=7)),
                ('table', models.IntegerField(default=None, null=True)),
                ('discount_percent', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default=0)),
                ('status_delivery', models.IntegerField(choices=[(1, 'delivery'), (0, 'eat_here')])),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_amount', models.IntegerField()),
                ('payment_status', models.IntegerField(choices=[(1, 'cash on delivery'), (2, 'credit'), (3, 'cash'), (4, 'transfer')], default=4)),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('status_order', models.IntegerField(choices=[(0, 'waiting'), (1, 'on cooking'), (2, 'on delivery'), (3, 'finish'), (4, 'void')], default=0)),
                ('status_drink', models.IntegerField(choices=[(0, 'waiting'), (1, 'on cooking'), (2, 'finish')], default=None, null=True)),
                ('status_food', models.IntegerField(choices=[(0, 'waiting'), (1, 'on cooking'), (2, 'finish')], default=None, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('point', models.IntegerField(blank=True, default=None, null=True)),
                ('cash', models.IntegerField(default=None, null=True)),
                ('change', models.IntegerField(default=None, null=True)),
                ('spen_time', models.TimeField(default=None, null=True)),
                ('reason', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_order', models.IntegerField(choices=[(0, 'waiting'), (1, 'on cooking'), (2, 'finish')], default=0)),
                ('code', models.CharField(max_length=100)),
                ('flavour_level', models.IntegerField(choices=[(0, 'none'), (1, 'low'), (2, 'medium'), (3, 'very')], null=True)),
                ('price_item', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L')], default='M', max_length=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(null=True)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=None, null=True, upload_to=pos.models.upload_to_payment, verbose_name='Image')),
                ('payment', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('descriptions', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_topping', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.OrderItem')),
            ],
        ),
    ]
