# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0003_auto_20160125_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
