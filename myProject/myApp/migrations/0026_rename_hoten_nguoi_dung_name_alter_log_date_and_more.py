# Generated by Django 4.0.3 on 2022-11-12 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_alter_log_date_alter_log_time_in'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nguoi_dung',
            old_name='hoten',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 13, 2, 32, 24, 178725)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2022, 11, 13, 2, 32, 24, 178725)),
        ),
    ]
