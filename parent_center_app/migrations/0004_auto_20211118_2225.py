# Generated by Django 3.2.9 on 2021-11-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent_center_app', '0003_auto_20211118_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id_admin',
            field=models.CharField(default='adm-18112021222545675291', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='mapel',
            name='id_mapel',
            field=models.CharField(default='mpl-18112021222545675291', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
