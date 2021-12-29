# Generated by Django 3.0.7 on 2021-12-29 04:44

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20211228_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type_topping',
        ),
        migrations.RemoveField(
            model_name='topping',
            name='update_at',
        ),
        migrations.AddField(
            model_name='product',
            name='topping_category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.ToppingCategory'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='img',
            field=models.ImageField(default=None, null=True, upload_to=product.models.upload_to_topping, verbose_name='Image'),
        ),
    ]
