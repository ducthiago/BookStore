# Generated by Django 4.0.3 on 2022-11-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0021_alter_nguoi_dung_thoigianvao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoi_dung',
            name='thoiginRA',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
