# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-09 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('lastActive', models.DateTimeField(auto_now=True)),
                ('firstPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameFirstPlayer', to=settings.AUTH_USER_MODEL)),
                ('secondPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameSecondPlayer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('byFirstPlayer', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game')),
            ],
        ),
    ]