# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isdelete', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xunda', models.CharField(max_length=20)),
                ('xuner', models.CharField(max_length=30)),
                ('zhaofei', models.CharField(max_length=20)),
                ('zhaoxun', models.CharField(max_length=20)),
                ('zhaozilong', models.CharField(max_length=20)),
            ],
        ),
    ]
