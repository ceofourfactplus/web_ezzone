# Generated by Django 3.0.7 on 2021-12-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20211227_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='type_category',
            field=models.IntegerField(choices=[(1, 'ของหวาน'), (2, 'เครื่องดื่ม'), (3, 'อาหาร'), (4, 'topping')]),
        ),
    ]
