# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hugs', '0009_auto_20170205_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='hugposting',
            name='ditched',
            field=models.BooleanField(default=False),
        ),
    ]
