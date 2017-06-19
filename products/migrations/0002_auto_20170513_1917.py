# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productDiscription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='productName',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
