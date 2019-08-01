# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-01 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('customer_type', models.IntegerField()),
                ('processor', models.CharField(max_length=10)),
                ('hdd', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('os', models.CharField(max_length=20)),
                ('sna1', models.CharField(max_length=30)),
                ('sna2', models.CharField(max_length=30)),
                ('sna3', models.CharField(max_length=30)),
                ('service_type', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]