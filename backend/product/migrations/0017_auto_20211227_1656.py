# Generated by Django 3.0.7 on 2021-12-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20211227_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
