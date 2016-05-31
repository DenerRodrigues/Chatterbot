# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='aiml',
            field=models.FilePathField(verbose_name=b'Aiml'),
        ),
    ]
