# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0002_auto_20160124_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='album',
            field=models.CharField(default='desconocido', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='end_time',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='solo',
            name='start_time',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
