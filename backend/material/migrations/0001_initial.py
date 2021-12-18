# Generated by Django 3.0.7 on 2021-12-18 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import material.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raw_material', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=material.models.upload_to_material, verbose_name='Image')),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('minimum', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PickUpMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pick_up_material_create_by', to=settings.AUTH_USER_MODEL)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.Material')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('type_category', models.CharField(max_length=30)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_category_create_by', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='material_category_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.MaterialCategory'),
        ),
        migrations.AddField(
            model_name='material',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='material',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='raw_material.Unit'),
        ),
        migrations.AddField(
            model_name='material',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='material_update_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AddMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='add_material_create_by', to=settings.AUTH_USER_MODEL)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='material.Material')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_material_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
