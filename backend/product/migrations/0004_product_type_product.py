# Generated by Django 3.0.7 on 2021-12-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211229_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type_product',
            field=models.IntegerField(choices=[(1, 'ของหวาน'), (2, 'เครื่องดื่ม'), (3, 'อาหาร')], default=3),
        ),
    ]
