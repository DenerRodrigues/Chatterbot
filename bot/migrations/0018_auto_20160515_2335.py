# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_auto_20160515_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 5, 16, 2, 35, 38, 698454, tzinfo=utc))),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='conversas',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='logo',
        ),
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 16, 2, 35, 38, 697682, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Conversas',
        ),
        migrations.AddField(
            model_name='conversation',
            name='chat',
            field=models.ForeignKey(to='bot.Chat'),
        ),
    ]
