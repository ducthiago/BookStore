# Generated by Django 4.0.3 on 2022-12-28 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0068_order_cart_items_alter_books_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
