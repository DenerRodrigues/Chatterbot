# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20160515_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 22, 59, 5, 743876, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chat',
            name='question',
            field=models.TextField(),
        ),
    ]
