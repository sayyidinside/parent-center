# Generated by Django 3.2.9 on 2021-12-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_center_app', '0025_auto_20211220_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaranspp',
            name='thn_ajar',
            field=models.CharField(default='2012/2022', max_length=10),
        ),
    ]