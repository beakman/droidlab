# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_auto_20161015_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
