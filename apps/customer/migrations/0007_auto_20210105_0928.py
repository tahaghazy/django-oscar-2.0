# Generated by Django 2.2.17 on 2021-01-05 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20210105_0928'),
        ('wishlists', '0004_auto_20210105_0928'),
        ('address', '0007_auto_20210105_0928'),
        ('voucher', '0008_auto_20210105_0928'),
        ('analytics', '0003_auto_20210105_0928'),
        ('payment', '0005_auto_20210105_0928'),
        ('auth', '0011_update_proxy_permissions'),
        ('order', '0008_auto_20210105_0928'),
        ('basket', '0009_auto_20210105_0928'),
        ('partner', '0005_auto_20181115_1953'),
        ('admin', '0004_auto_20210105_0928'),
        ('reviews', '0005_auto_20210105_0928'),
        ('customer', '0006_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CUStom',
        ),
        migrations.AlterField(
            model_name='email',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL, to_field='id', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
        migrations.AlterField(
            model_name='productalert',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL, to_field='id', verbose_name='User'),
        ),
    ]