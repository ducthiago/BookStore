# Generated by Django 4.0.3 on 2022-12-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0073_order_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_items',
        ),
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myApp.cartitem'),
        ),
    ]
