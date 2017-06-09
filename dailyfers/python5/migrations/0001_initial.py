# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zhangfei', models.CharField(max_length=20)),
                ('guangyu', models.CharField(max_length=20)),
                ('zilong', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isdelete', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='bookc',
            name='key',
            field=models.ForeignKey(to='python5.Books'),
        ),
    ]
