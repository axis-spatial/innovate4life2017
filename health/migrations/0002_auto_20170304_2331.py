# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 20:31
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthfacility',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
