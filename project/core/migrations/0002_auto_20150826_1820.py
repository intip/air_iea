# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processing',
            name='status',
            field=models.TextField(default=1, db_index=True, verbose_name=b'Status', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='processing',
            name='air_file',
            field=models.TextField(db_index=True, verbose_name=b'AIR FILE', blank=True),
        ),
        migrations.AlterField(
            model_name='processing',
            name='iea_file',
            field=models.TextField(db_index=True, verbose_name=b'IEA FILE', blank=True),
        ),
    ]
