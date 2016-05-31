#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.shortcuts import render
from model.bot import Bot
from model.chat import Chat
from model.conversation import Conversation
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from Chatterbot.settings import MEDIA_ROOT
import random
import aiml
import os


# Create your views here.

def page_index(request):
    return render(request, "index.html", {})


def page_chat(request, context=None):
    if not context:
        context = {'bots': get_bots()}
    return render(request, "chat.html", context)


def get_bots():
    try:
        bots = Bot.objects.all().order_by("name")
    except ObjectDoesNotExist:
        bots = None

    return bots


@csrf_exempt
def get_chat(request):
    question = request.POST['input-chat'] or ''
    bot_selected = Bot.objects.get(name=request.POST['select-bot'])
    chat_id = request.POST['chat_id'] or 0
    date = timezone.now()

    try:
        chat = Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        chat = None

    if not chat:
        chat = Chat.objects.create(log=bot_selected, bot=bot_selected)

    answer = get_answer(bot_selected, question)
    Conversation.objects.create(chat=chat, question=question, answer=answer)
    create_log(chat, question, answer, date)

    context = {
        'chat_id': chat.id, 'chat': Conversation.objects.filter(chat=chat),
        'bots': get_bots(), 'bot_selected': bot_selected, 'date': date,
    }

    return page_chat(request, context)


def create_log(chat, question, answer, date):
    log = remove_accents(chat.log)
    log += remove_accents("\n%s Question: %s:\n%s Answer: %s:" %
                          (date, question.encode('utf-8', 'strict'),
                           date, answer))
    chat.log = log
    chat.save()

    return True


def get_answer(bot, question, format_string=False):
    aiml_file = os.path.join(MEDIA_ROOT, os.path.split(bot.aiml.url)[1])

    if format_string:
        return get_answer_formated(aiml_file, question)

    aiml_kernel = aiml.Kernel()
    aiml_kernel.setTextEncoding('UTF-8')

    aiml_kernel.learn(aiml_file)
    answer = aiml_kernel.respond(question.upper())

    return answer or "Vamos falar sobre o ENEM?"


def get_answer_formated(aiml_file, question):
    answer = "Vamos falar sobre o ENEM?"
    aiml_text = open(aiml_file).read()
    categories = aiml_text.split('category')
    question_name = None

    if remove_accents(question[:10].lower().encode('utf-8', 'strict')) == 'meu nome e':
        question_name = remove_accents(question[:10].lower().encode('utf-8', 'strict'))

    category = get_category(categories, question, question_name)

    if category:
        template = category.split('template')[1]
        if question_name:
            answer = template.split('>')[6][:13] + question[11:] + remove_accents(
                template.split('>')[8][:-4].encode('utf-8', 'strict'))
        elif 'random' not in template:
            answer = template[1][3:-2]
        else:
            list_template = template.split('li>')[1:-1]
            for i in list_template:
                if len(i.replace(' \r\n <', '').replace('\r\n <', '')) == 0:
                    list_template.remove(i)
            answer = random.choice(list_template)[:-2]

    return answer


def get_category(categories, question, question_name=None):
    category = None

    for category in categories:
        if question_name:
            if '<pattern>' + question_name in remove_accents(
                    category.lower().encode('utf-8', 'strict')):
                break
        elif question[-1:] == '?':
            if remove_accents(question[:-1].lower().encode('utf-8', 'strict')) in remove_accents(
                    category.lower().encode('utf-8', 'strict')):
                break
        elif remove_accents(question.lower().encode('utf-8', 'strict')) in remove_accents(
                category.lower().encode('utf-8', 'strict')):
            break
        else:
            category = None

    return category


def remove_accents(text, cod='utf-8'):
    from unicodedata import normalize, category
    return unicode(filter(lambda c: category(c) != 'Mn', normalize('NFKD', str(text).decode(cod))))
