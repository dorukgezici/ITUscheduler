# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170811_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='crn',
            field=models.PositiveIntegerField(),
        ),
    ]
