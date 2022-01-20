# Generated by Django 4.0.1 on 2022-01-20 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raw_material', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricerawmaterial',
            name='avg_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pricerawmaterial',
            name='last_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='update_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_update_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
