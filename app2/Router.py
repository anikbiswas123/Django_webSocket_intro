from django.urls import path 

from .consummer import *

websocket_urlpatterns=[
    path('ws/sc/',MySyncConsumer.as_asgi()),
    path('ws/ac/',MyAsyncConsumer.as_asgi()),
]