#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""Chatterbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin


from mezzanine.core.views import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'bot.views.page_index'),
                       url(r'^chat/', 'bot.views.page_chat'),
                       url(r'^chat_action/', 'bot.views.get_chat'),
                       url("^$", direct_to_template, {"template": "index.html"}, name="home"),
                       url("^", include("mezzanine.urls")),
                       )
