# -*- coding: utf-8 -*-
from robot import Bot
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = Bot('localhost:8000', 'suap')
        for message in bot.messages:
            message.repply(message.text)