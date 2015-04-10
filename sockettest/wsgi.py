"""
WSGI config for sockettest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from gevent import monkey
monkey.patch_all()

import os
from psycogreen.gevent import patch_psycopg

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sockettest.settings")
patch_psycopg()

application = get_wsgi_application()

if __name__ == '__main__':
    from socketio.server import SocketIOServer
    server = SocketIOServer(('', 8000), application, resource="socket.io")
    server.serve_forever()