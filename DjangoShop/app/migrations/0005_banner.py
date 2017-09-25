# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170910_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannername', models.CharField(max_length=50)),
                ('bannerimg', models.FileField(upload_to='banner/')),
                ('bannerdate', models.DateTimeField(auto_now_add=True)),
                ('bannerdesc', models.TextField()),
            ],
        ),
    ]