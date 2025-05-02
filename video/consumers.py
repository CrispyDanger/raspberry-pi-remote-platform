import asyncio
import cv2
import json
from aiortc import RTCSessionDescription, RTCPeerConnection, VideoStreamTrack
from channels.generic.websocket import AsyncWebsocketConsumer
from av import VideoFrame


class CameraStreamTrack(VideoStreamTrack):
    def __init__(self):
        super().__init__()
        print("Starting camera...")
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open video device.")

    async def recv(self):
        pts, time_base = await self.next_timestamp()

        ret, frame = self.cap.read()
        if not ret:
            await asyncio.sleep(1/30)
            return await self.recv()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_frame = VideoFrame.from_ndarray(frame, format="rgb24")
        video_frame.pts = pts
        video_frame.time_base = time_base
        return video_frame

    def release(self):
        if self.cap.isOpened():
            self.cap.release()
            print("Camera released.")


class WebRTCConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.pc = None
        self.camera = None

    async def disconnect(self, close_code):
        if self.pc:
            await self.pc.close()
        if self.camera:
            self.camera.release()

    async def receive(self, text_data):
        data = json.loads(text_data)

        if not self.pc:
            self.pc = RTCPeerConnection()
            self.camera = CameraStreamTrack()
            self.pc.addTrack(self.camera)

        offer = RTCSessionDescription(
            sdp=data["sdp"],
            type=data["type"]
        )

        await self.pc.setRemoteDescription(offer)
        answer = await self.pc.createAnswer()
        await self.pc.setLocalDescription(answer)

        await self.send(text_data=json.dumps({
            "sdp": self.pc.localDescription.sdp,
            "type": self.pc.localDescription.type
        }))
