# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_mgr_app', '0001_initial'),
        ('alert_config_app', '0003_trigger_pv'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='owner',
            field=models.ManyToManyField(to='account_mgr_app.Profile'),
        ),
        migrations.AddField(
            model_name='alert',
            name='subscriber',
            field=models.ManyToManyField(related_name='subscriptions', to='account_mgr_app.Profile'),
        ),
    ]
