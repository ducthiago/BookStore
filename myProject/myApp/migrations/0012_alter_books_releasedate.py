# Generated by Django 4.0.3 on 2022-10-08 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_alter_books_releasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='releaseDate',
            field=models.CharField(default=None, max_length=200),
        ),
    ]