#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone
from chat import Chat


# Create your model here.

class Conversation(models.Model):
    chat = models.ForeignKey(Chat)
    date = models.DateTimeField(default=timezone.now())
    question = models.TextField()
    answer = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.chat, self.date)

    class Meta:
        app_label = 'bot'
