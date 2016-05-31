# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20160514_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='aiml',
            field=models.BinaryField(verbose_name=b'Aiml'),
        ),
    ]
