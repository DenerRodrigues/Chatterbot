# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_auto_20160515_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='bot',
            field=models.OneToOneField(to='bot.Bot'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 20, 27, 17, 952220, tzinfo=utc)),
        ),
    ]
