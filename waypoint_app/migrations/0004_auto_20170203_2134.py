# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waypoint_app', '0003_auto_20170104_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisis',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='crisis',
            name='description_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='food',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='food',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='food',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='legal',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='legal',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='legal',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='medical',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medical',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='medical',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='shelter',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shelter',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='shelter',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='transportation',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transportation',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
        migrations.AddField(
            model_name='transportation',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=30),
        ),
    ]
