# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0005_auto_20161015_2024'),
        ('users', '0002_auto_20161011_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experiments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='experiments.Experiment'),
        ),
    ]
