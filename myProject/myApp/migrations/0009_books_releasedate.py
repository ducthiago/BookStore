# Generated by Django 4.0.3 on 2022-10-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_alter_books_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='releaseDate',
            field=models.TextField(blank=True, null=True),
        ),
    ]