# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='Game',
        ),
        migrations.AddField(
            model_name='game',
            name='viisted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='voted_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='voted_person',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='option',
            name='game',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='vote.Game'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(blank=True, default=b'', max_length=1024),
        ),
    ]