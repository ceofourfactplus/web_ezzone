# Generated by Django 3.0.7 on 2022-01-13 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0013_auto_20220113_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtopping',
            old_name='amount',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='packageitem',
            old_name='amount',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='voucher',
            old_name='amount',
            new_name='qty',
        ),
    ]
