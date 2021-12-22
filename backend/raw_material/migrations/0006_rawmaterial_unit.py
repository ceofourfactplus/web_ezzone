# Generated by Django 3.0.7 on 2021-12-21 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0005_auto_20211221_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='raw_material.Unit'),
            preserve_default=False,
        ),
    ]