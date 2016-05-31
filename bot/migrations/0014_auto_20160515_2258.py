# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_auto_20160515_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='answer',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='chat',
            name='question',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 22, 58, 54, 225503, tzinfo=utc)),
        ),
    ]
