# Generated by Django 4.0.3 on 2022-11-12 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0027_alter_log_date_alter_log_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 2, 35, 26, 931300)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2022, 11, 13, 2, 35, 26, 931300)),
        ),
        migrations.AlterField(
            model_name='nguoi_dung',
            name='thoigianVAO',
            field=models.TimeField(default=datetime.datetime(2022, 11, 13, 2, 35, 26, 930299)),
        ),
    ]
