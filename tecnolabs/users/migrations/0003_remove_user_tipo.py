# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipo',
        ),
    ]
