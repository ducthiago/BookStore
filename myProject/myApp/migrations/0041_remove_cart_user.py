# Generated by Django 4.0.3 on 2022-11-21 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0040_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
