# Generated by Django 3.0.7 on 2021-12-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211219_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]