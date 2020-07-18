import json
import time
from socket import timeout
from http.client import HTTPConnection, RemoteDisconnected
from json.decoder import JSONDecodeError


def request(host, url, data=None, timeout=None):
    conn = HTTPConnection(host, timeout=timeout)
    body = data and json.dumps(data) or None
    try:
        conn.request("GET", '/{}'.format(url), body=body)
        response = conn.getresponse()
        data = response.read()
        return json.loads(data)
    finally:
        conn.close()

class Message():
    def __init__(self, host, service, user, text, uuid):
        self.host = host
        self.service = service
        self.user = user
        self.text = text
        self.uuid = uuid

    def repply(self, text):
        request(self.host, self.service, dict(user=self.user, text=text, uuid=self.uuid))

    def __str__(self):
        return '{} {}'.format(self.user, self.text)

class Bot():
    def __init__(self, host, service, timeout=None):
        self.host = host
        self.service = service
        self.timeout = timeout

    @property
    def message(self):
        data = request(self.host, self.service)
        if 'user' in data:
            return Message(host=self.host, service=self.service, user=data['user'], text=data['text'], uuid=data['uuid'])
        else:
            return self.message

    @property
    def messages(self):
        while True:
            try:
                yield self.message
            except timeout:
                pass
            except RemoteDisconnected:
                print('The server disconnected! Trying to connect in 10 secs...')
                time.sleep(10)
            except ConnectionRefusedError:
                print('The server is offline! Trying to connect in 10 secs...')
                time.sleep(10)
            except JSONDecodeError:
                print('The response is invalid! Trying again in 10 secs...')
                time.sleep(10)
            except KeyboardInterrupt:
                print('Bye!!!!')
                break
