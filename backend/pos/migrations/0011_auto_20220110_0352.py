# Generated by Django 3.0.7 on 2022-01-10 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_topping_old_product'),
        ('pos', '0010_auto_20220109_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sale_channel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.SaleChannel'),
        ),
    ]