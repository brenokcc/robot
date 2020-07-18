# -*- coding: utf-8 -*-
import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # import docker
        # client = docker.from_env()
        # container = None
        # try:
        #     container = client.containers.run(
        #         image='whatsappweb',
        #         name='whatsappweb',
        #         remove=True,
        #         ports={'9999/tcp': '9999'},
        #         volumes={'{}/.whatsapp'.format(os.environ['HOME']): {'bind': '/var/whatsapp/', 'mode': 'rw'}},
        #         detach=True)
        #     for message in container.logs(stream=True):
        #         print(message.decode())
        #     print(111)
        # except KeyboardInterrupt:
        #     print('Bye!')
        # finally:
        #     container.stop()
        try:
            os.system('docker run --name=whatsapp --rm -it -v /Users/breno/.whatsapp:/var/whatsapp -d -p 9999:9999 whatsappweb')
            os.system('docker logs -f whatsapp')
        except KeyboardInterrupt:
            print('The container "whatsapp" is still runnig! Type "docker stop whatsapp" to stop it.')