# Generated by Django 4.0.3 on 2022-10-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_user_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='created',
        ),
        migrations.RemoveField(
            model_name='books',
            name='updated',
        ),
        migrations.AddField(
            model_name='books',
            name='bookName',
            field=models.CharField(default='Thứ anh đang mong chờ', max_length=50),
        ),
    ]