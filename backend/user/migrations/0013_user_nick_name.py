# Generated by Django 3.0.7 on 2021-12-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20211216_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]