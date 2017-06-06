# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=100)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gpic', models.ImageField(upload_to=b'goods')),
                ('gjianjie', models.CharField(max_length=200)),
                ('gunit', models.CharField(max_length=50)),
                ('gjieshao', tinymce.models.HTMLField()),
                ('gcilck', models.IntegerField(default=0)),
                ('gkuzhu', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='python.TypeInof'),
        ),
    ]
