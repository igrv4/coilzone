# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20170610_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='price_per_item',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productincart',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
