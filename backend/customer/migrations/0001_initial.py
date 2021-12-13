# Generated by Django 3.0.7 on 2021-12-12 06:06

import customer.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to=customer.models.upload_to_customer, verbose_name='Image')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('line_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_joined', models.DateTimeField(auto_now_add=True)),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.Customer')),
            ],
        ),
    ]