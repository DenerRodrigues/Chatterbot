# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20160514_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='aiml',
            field=models.BinaryField(default=b'\x08', max_length=10),
        ),
    ]
