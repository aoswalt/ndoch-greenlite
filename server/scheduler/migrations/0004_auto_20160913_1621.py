# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20160913_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vertex',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 13, 16, 21, 50, 918012, tzinfo=utc)),
        ),
    ]
