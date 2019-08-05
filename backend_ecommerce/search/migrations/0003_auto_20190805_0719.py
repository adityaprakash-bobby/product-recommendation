# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-05 07:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_timestamp'),
        ('search', '0002_savedsearches_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedsearches',
            name='search',
        ),
        migrations.RemoveField(
            model_name='savedsearches',
            name='product_viewed',
        ),
        migrations.AddField(
            model_name='savedsearches',
            name='product_viewed',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='savedsearches',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
