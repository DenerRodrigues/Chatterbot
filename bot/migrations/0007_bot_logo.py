# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20160514_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
