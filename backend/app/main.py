import asyncio
import json
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .models import *

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        car1 = Vehicle(1, 5)
        while True:
            car1.speed = 2
            while car1.speed < 5:
                car1.accelerate()
                await websocket.send_json(car1.to_dict())
                await asyncio.sleep(0.5)
            
            while car1.speed > 0:
                car1.decelerate()
                await websocket.send_json(car1.to_dict())
                await asyncio.sleep(0.5)
    except Exception as e:
        print(f"WebSocket connection closed: {e}")