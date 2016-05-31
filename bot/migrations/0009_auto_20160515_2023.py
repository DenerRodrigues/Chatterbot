# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
