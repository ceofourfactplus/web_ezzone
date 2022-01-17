# Generated by Django 3.0.7 on 2022-01-16 18:35

import consignment.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddConsignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consigner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('line_id', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('id_card', models.CharField(max_length=13)),
                ('birth_date', models.DateField()),
                ('cradit_cart', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='ConsignmentPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConsignmentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=None, null=True, upload_to=consignment.models.upload_to_consignment, verbose_name='Image')),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(0, 'สินค้าหมด'), (1, 'สินค้าเกือบหมด'), (2, 'สินค้าพร้อมขาย')], default=2)),
                ('remain', models.IntegerField(default=0)),
                ('minimum', models.IntegerField(default=0)),
                ('maximum', models.IntegerField(default=None, null=True)),
                ('share', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceConsignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('consignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consignment.ConsignmentProduct')),
            ],
        ),
    ]
