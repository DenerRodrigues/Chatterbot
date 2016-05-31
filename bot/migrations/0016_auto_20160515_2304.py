# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_auto_20160515_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 5, 15, 23, 4, 13, 546521, tzinfo=utc))),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 15, 23, 4, 13, 545868, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='conversas',
            name='chat',
            field=models.ForeignKey(to='bot.Chat'),
        ),
    ]
