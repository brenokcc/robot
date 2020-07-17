# -*- coding: utf-8 -*-
import socket
import json
import time
import threading
import datetime
from whatsapp.models import IncomeMessage, OutcomeMessage
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 9999))
        print('Connection opened!')
        def send():
            while True:
                for message in OutcomeMessage.objects.filter(delivered=False):
                    text = json.dumps({'to': message.user, 'body': message.text}).encode()
                    print('>>> {} {}'.format(datetime.datetime.now(), text))
                    client.send(text)
                    message.delivered = True
                    message.save()
                time.sleep(5)
        thread = threading.Thread(target=send, daemon=True)
        thread.start()

        def receive():
            l = []
            while True:
                c = client.recv(1)
                if c == b'\xe2':
                    text = b''.join(l).decode('utf-8', 'ignore')
                    return text
                else:
                    l.append(c)

        try:
            while True:
                text = receive()
                print('<<< {} {}'.format(datetime.datetime.now(), text))
                data = json.loads(text)
                IncomeMessage.objects.create(user=data['from'], text=data['body'])
        except KeyboardInterrupt:
            client.close()
            print('Connection closed!')