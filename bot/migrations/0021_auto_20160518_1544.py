# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_auto_20160518_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='image',
            new_name='photo',
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 44, 3, 630271, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 18, 44, 3, 630891, tzinfo=utc)),
        ),
    ]
