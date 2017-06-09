# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0002_auto_20170606_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsinfo',
            old_name='gkuzhu',
            new_name='gkucun',
        ),
        migrations.RemoveField(
            model_name='goodsinfo',
            name='gcilck',
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
    ]
