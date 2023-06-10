# Generated by Django 4.0.3 on 2022-10-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_books_created_remove_books_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='books',
            name='bookName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
