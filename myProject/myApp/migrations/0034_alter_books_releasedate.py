# Generated by Django 4.0.3 on 2022-11-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0033_delete_log_delete_nguoi_dung_alter_books_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='releaseDate',
            field=models.IntegerField(),
        ),
    ]
