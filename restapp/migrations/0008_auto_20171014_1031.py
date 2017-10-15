# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0007_auto_20171013_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('infoSection', models.CharField(choices=[('1', 'Information'), ('2', 'Schedule'), ('3', 'Placement')], max_length=5)),
                ('infoType', models.CharField(choices=[('parent', 'Title'), ('child', 'Description')], max_length=20)),
                ('semester', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='link',
            name='notesType',
            field=models.CharField(choices=[('1', 'Class Notes'), ('2', 'Question Bank'), ('3', 'Staff Notes'), ('4', 'Test Questions')], max_length=5),
        ),
    ]
