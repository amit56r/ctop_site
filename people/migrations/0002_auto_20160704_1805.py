# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='position',
            field=models.CharField(choices=[('PROF', 'Professor'), ('STUDENT', 'Student'), ('STAFF', 'Staff')], default='STUDENT', max_length=10),
        ),
    ]
