# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_context_member1'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='member2',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
