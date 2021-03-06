# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=40)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('bu', models.CharField(blank=True, max_length=40)),
                ('is_enabled', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
