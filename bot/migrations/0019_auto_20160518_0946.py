# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_auto_20160515_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='aiml',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 12, 46, 44, 592931, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 12, 46, 44, 593669, tzinfo=utc)),
        ),
    ]
