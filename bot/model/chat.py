#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone
from bot import Bot


# Create your model here.

class Chat(models.Model):
    bot = models.ForeignKey(Bot)
    date = models.DateTimeField(default=timezone.now())
    log = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.bot, self.date)

    class Meta:
        app_label = 'bot'
