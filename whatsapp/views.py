import json
import time
from whatsapp.models import IncomeMessage, OutcomeMessage, Service, UserService
from django.http import HttpResponse, HttpResponseNotAllowed


def index(request, service):
    Service.objects.get_or_create(name=service)
    if Service.objects.filter(name=service).exists():
        if request.body:
            message = json.loads(request.body.decode())
            user = message['user']
            text = message['text']
            OutcomeMessage.objects.create(user=user, text=text)
            return HttpResponse(json.dumps({}))
        else:
            timeout = int(request.GET.get('timeout', 0) or 60)
            while timeout > 0:
                message = IncomeMessage.objects.filter(delivered=False).first()
                if message:
                    message.delivered = True
                    message.save()
                    # the user typed the key-word (service name)
                    if Service.objects.filter(name=message.text).exists():
                        UserService.objects.filter(user=message.user).delete()
                        UserService.objects.create(user=message.user, service=service)
                        data = dict(user=message.user, text=message.text)
                        return HttpResponse(json.dumps(data))
                    # the user is not binded to a service
                    elif UserService.objects.filter(user=message.user, service=service).first() is None:
                        text = 'Olá! Para conversar com você, preciso que me informe a palavra-chave.'
                        OutcomeMessage.objects.create(user=message.user, text=text)
                    # if the user is saying good-bye
                    elif message.text.lower().startswith('tchau'):
                        UserService.objects.filter(user=message.user).delete()
                        text = 'Foi um prazer atendê-lo! Digite a palavra-chave sempre que quiser falar comigo.'
                        OutcomeMessage.objects.create(user=message.user, text=text)
                    # forward the message to the client
                    else:
                        data = dict(user=message.user, text=message.text)
                        return HttpResponse(json.dumps(data))
                timeout = timeout-3
                time.sleep(3)
        return HttpResponse(json.dumps({}))
    return HttpResponseNotAllowed()

