import sys
import os
import docker


COMMAND = sys.argv[1]
BASE_DIR = os.path.dirname(__file__)
DOCKER_FILE = os.path.join(BASE_DIR, 'Dockerfile')

def build():
    client = docker.from_env()
    client.images.build(path=BASE_DIR, tag='whatsappweb', quiet=False)

def run():
    # docker run --name=whatsappweb --rm -it -p 8000:8000 -p 8080:8080 whatsappweb sh
    pass

def stop():
    pass

if COMMAND == 'build':
    build()
