# Generated by Django 3.0.7 on 2021-12-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_id_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_card',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]