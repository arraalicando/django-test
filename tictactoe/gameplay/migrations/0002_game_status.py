# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-09 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player to Move'), ('S', 'Second Player to Move'), ('FW', 'First Player Wins'), ('SW', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=2),
        ),
    ]
