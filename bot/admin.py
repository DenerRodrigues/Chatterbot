#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.contrib import admin
from model.bot import Bot
from model.chat import Chat
from model.conversation import Conversation


# Register your model here.


class BotAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_editable = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ChatAdmin(admin.ModelAdmin):
    list_display = ["bot", "date"]
    list_filter = ["bot", "date"]
    search_fields = ["bot", "date"]


class ConversationAdmin(admin.ModelAdmin):
    list_display = ["chat", "date"]
    list_filter = ["chat", "date"]
    search_fields = ["chat", "date"]


admin.site.register(Bot, BotAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Conversation, ConversationAdmin)
