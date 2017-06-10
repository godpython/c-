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
                ('guanyu', models.CharField(max_length=20)),
                ('zhafei', models.CharField(max_length=20)),
                ('zilong', models.CharField(max_length=20)),
                ('xuda', models.CharField(max_length=20)),
                ('xuer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Inof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='key',
            field=models.ForeignKey(to='test1.Inof'),
        ),
    ]
