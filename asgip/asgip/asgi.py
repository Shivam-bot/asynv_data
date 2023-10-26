"""
ASGI config for asgip project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from asgia.consumer import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asgip.settings')

application = get_asgi_application()

ws_pattern = [
    path('ws/test/<str:user_name>',TestConsumer.as_asgi()),
    path('ws/new/',NewConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': application,
    'websocket': URLRouter(ws_pattern)
})
