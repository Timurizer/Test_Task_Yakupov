# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='note_manager.User'),
            preserve_default=False,
        ),
    ]
