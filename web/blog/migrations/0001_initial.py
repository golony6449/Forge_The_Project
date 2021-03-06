# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('primaryLanguage', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('postID', models.IntegerField(primary_key=True, serialize=False)),
                ('contents', models.TextField()),
                ('postDate', models.DateField()),
                ('userID', models.CharField(max_length=10)),
            ],
        ),
    ]
