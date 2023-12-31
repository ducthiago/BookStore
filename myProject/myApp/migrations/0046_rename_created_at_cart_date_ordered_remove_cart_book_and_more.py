# Generated by Django 4.0.3 on 2022-11-22 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0045_alter_cart_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created_at',
            new_name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='book',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.cart')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Số lượng')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.books', verbose_name='Cuốn sách')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.cart')),
            ],
        ),
    ]
