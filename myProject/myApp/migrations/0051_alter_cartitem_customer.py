# Generated by Django 4.0.3 on 2022-11-22 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0050_cartitem_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='customer',
            field=models.ForeignKey(blank=True, default=123, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
