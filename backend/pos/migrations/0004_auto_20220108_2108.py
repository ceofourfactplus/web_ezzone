# Generated by Django 3.0.7 on 2022-01-08 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_auto_20220108_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'cash on delivery'), (2, 'credit'), (3, 'paid')], default=3),
        ),
    ]