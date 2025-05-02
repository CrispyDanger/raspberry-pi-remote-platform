from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .utils import write_operation


class DroneControlConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket connected!")

    async def disconnect(self, close_code):
        print("WebSocket disconnected!")

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "forward":
            print("Moving Forward")
            write_operation('forward', 1.0)
        elif action == "stop":
            print("Stopping")
