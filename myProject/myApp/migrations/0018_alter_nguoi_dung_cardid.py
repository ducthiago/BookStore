# Generated by Django 4.0.3 on 2022-11-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_alter_nguoi_dung_cardid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoi_dung',
            name='cardID',
            field=models.CharField(max_length=11),
        ),
    ]
