# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['index', 'id'], 'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='\u4e2a\u4eba\u7f51\u9875\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6b21\u6570'),
        ),
    ]
