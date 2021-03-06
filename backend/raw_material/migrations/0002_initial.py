# Generated by Django 4.0.1 on 2022-01-20 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raw_material', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='supplier',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='supplier_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receiptrawmaterialdetail',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipt_raw_material_detail_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receiptrawmaterialdetail',
            name='raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.rawmaterial'),
        ),
        migrations.AddField(
            model_name='receiptrawmaterialdetail',
            name='receipt_raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raw_material.receiptrawmaterial'),
        ),
        migrations.AddField(
            model_name='receiptrawmaterialdetail',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.supplier'),
        ),
        migrations.AddField(
            model_name='receiptrawmaterialdetail',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_raw_material_detail_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receiptrawmaterial',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipt_raw_material_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receiptrawmaterial',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.supplier'),
        ),
        migrations.AddField(
            model_name='receiptrawmaterial',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_raw_material_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.rawmaterialcategory'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='unit_l',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_unit_l', to='raw_material.unit'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='unit_m',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_unit_m', to='raw_material.unit'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='unit_s',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_unit_s', to='raw_material.unit'),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='update_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='raw_material_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pricerawmaterial',
            name='raw_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.rawmaterial'),
        ),
        migrations.AddField(
            model_name='pricerawmaterial',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.supplier'),
        ),
        migrations.AddField(
            model_name='pricerawmaterial',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.unit'),
        ),
        migrations.AddField(
            model_name='po',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='po',
            name='raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.rawmaterial'),
        ),
        migrations.AddField(
            model_name='po',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.supplier'),
        ),
        migrations.AddField(
            model_name='po',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.unit'),
        ),
        migrations.AddField(
            model_name='pickuprawmaterial',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pick_up_raw_material_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pickuprawmaterial',
            name='raw_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.rawmaterial'),
        ),
        migrations.AddField(
            model_name='pickuprawmaterial',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.unit'),
        ),
    ]
