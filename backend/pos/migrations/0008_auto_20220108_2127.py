# Generated by Django 3.0.7 on 2022-01-08 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='conignment',
            new_name='consignment',
        ),
    ]
