# Generated by Django 3.0.7 on 2021-12-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0004_remove_supplier_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='google_map',
            field=models.URLField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
