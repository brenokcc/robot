import requests, threading, queue
from http.server import HTTPServer, BaseHTTPRequestHandler

httpd = None
q = queue.Queue()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        q.put(data.decode())
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')
    def log_message(self, format, *args):
        return


def send(data):
    requests.post('http://127.0.0.1:8080', data=data)

def receive():
    global httpd
    if httpd is None:
        httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
        threading.Thread(target=lambda:httpd.serve_forever(), daemon=True).start()
    while True:
        yield q.get()


# for data in receive():
#    send(data)


