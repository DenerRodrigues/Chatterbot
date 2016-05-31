#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.db import models


# Create your model here.

class Bot(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nome")
    aiml = models.FileField()
    photo = models.ImageField(verbose_name="Foto", null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'bot'
