# Generated by Django 4.0.3 on 2022-11-12 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_rename_hoten_nguoi_dung_name_alter_log_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 2, 32, 29, 994882)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2022, 11, 13, 2, 32, 29, 994882)),
        ),
    ]
