# Generated by Django 3.0.7 on 2021-12-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0002_auto_20211228_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptrawmaterialdetail',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='receiptrawmaterialdetail',
            name='remark',
            field=models.TextField(blank=True),
        ),
    ]
