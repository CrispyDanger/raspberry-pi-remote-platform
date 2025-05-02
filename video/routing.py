
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/video/", consumers.WebRTCConsumer.as_asgi()),
]
