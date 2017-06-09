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
                ('isdelete', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wushu', models.CharField(max_length=20)),
                ('laohu', models.CharField(max_length=20)),
                ('xunda', models.CharField(max_length=20)),
                ('xuner', models.CharField(max_length=20)),
                ('guangyu', models.CharField(max_length=20)),
                ('zhaofei', models.CharField(max_length=20)),
                ('zhaoyun', models.CharField(max_length=20)),
            ],
        ),
    ]
