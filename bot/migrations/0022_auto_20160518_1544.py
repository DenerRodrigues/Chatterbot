# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_auto_20160518_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='photo',
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 44, 55, 528398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 44, 55, 529152, tzinfo=utc)),
        ),
    ]
