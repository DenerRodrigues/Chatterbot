# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_bot_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 5, 15, 20, 22, 16, 862988))),
                ('log', models.TextField()),
                ('bot', models.ForeignKey(to='bot.Bot')),
            ],
        ),
    ]
