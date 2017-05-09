# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=26)),
                ('counts', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'words',
            },
        ),
    ]
