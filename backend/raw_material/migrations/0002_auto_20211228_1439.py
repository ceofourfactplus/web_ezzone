# Generated by Django 3.0.7 on 2021-12-28 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='maximum',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='minimum',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='remain',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name='PriceRawMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('last_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('raw_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.RawMaterial')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.Supplier')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='raw_material.Unit')),
            ],
        ),
    ]
