# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170909_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='edate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='epic',
            field=models.FileField(upload_to='emp/'),
        ),
    ]
