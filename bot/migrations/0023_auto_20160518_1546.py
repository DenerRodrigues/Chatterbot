# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0022_auto_20160518_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 46, 23, 404626, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 46, 23, 405228, tzinfo=utc)),
        ),
    ]
