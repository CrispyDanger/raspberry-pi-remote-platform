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

        match action:
            case 'forward':
                write_operation('forward')
            case 'right':
                write_operation('right')
            case 'left':
                write_operation('left')
            case 'backward':
                write_operation('backward')
            case 'stop':
                write_operation('stop')
