# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='name',
            field=models.CharField(blank=True, default=b'', max_length=16),
        ),
    ]