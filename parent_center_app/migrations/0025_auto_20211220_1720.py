# Generated by Django 3.2.9 on 2021-12-20 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_center_app', '0024_auto_20211220_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelas',
            name='jurusan',
            field=models.CharField(choices=[('TITL', 'Teknik Intalasi Tenaga Listrik'), ('TP', 'Teknik Pemesinan'), ('TKR', 'Teknik Kendaraan Ringan'), ('TKJ', 'Teknik Komputer Jaringan'), ('RPL', 'Rekayasa Perangkat Lunak'), ('TBSM', 'Teknik dan Bisnis Sepeda Motor')], default='TITL', max_length=30),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='no_kelas',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]