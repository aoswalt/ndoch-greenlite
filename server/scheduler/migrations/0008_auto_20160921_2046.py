# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20160921_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vertex',
            name='label',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]
