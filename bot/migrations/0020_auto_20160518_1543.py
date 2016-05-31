# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0019_auto_20160518_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 43, 16, 156551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 43, 16, 157157, tzinfo=utc)),
        ),
    ]
