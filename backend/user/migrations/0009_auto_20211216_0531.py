# Generated by Django 3.0.7 on 2021-12-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_user_is_banned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_owner',
            field=models.IntegerField(default=False),
        ),
    ]
