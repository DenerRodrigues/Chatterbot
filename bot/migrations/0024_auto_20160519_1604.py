# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0023_auto_20160518_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 19, 4, 59, 582632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 19, 4, 59, 583249, tzinfo=utc)),
        ),
    ]
