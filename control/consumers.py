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
        speed = data.get("speed")

        match action:
            case 'forward':
                write_operation('forward', speed)
            case 'right':
                write_operation('right', speed)
            case 'left':
                write_operation('left', speed)
            case 'backward':
                write_operation('backward', speed)
            case 'stop':
                write_operation('stop')
