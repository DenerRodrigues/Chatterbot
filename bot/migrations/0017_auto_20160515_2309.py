# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0016_auto_20160515_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='question',
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 23, 9, 24, 766330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversas',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 23, 9, 24, 766985, tzinfo=utc)),
        ),
    ]
