# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
