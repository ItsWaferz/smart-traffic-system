from enum import Enum
import uuid

class LightColor(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"

class TrafficLight:
    def __init__(self, id: int, lane: str):
        self.id = id
        self.lane = lane
        self.color = LightColor.RED
        self.timer = 0

    def change_color(self, new_color: LightColor):
        self.color = new_color
        self.timer = 0

    def to_dict(self):
        return {
            "id": self.id,
            "lane": self.lane,
            "color": self.color.value,
            "timer": self.timer
        }
    
class Vehicle:
    def __init__(self, lane: int, speed: float = 5.0):
        self.id = str(uuid.uuid4())[:8]
        self.lane = lane
        self.speed = speed
        self.wainting_time = 0

        self.x = 0
        self.y = 0
        self.hasPassed = False

    def accelerate(self):
        self.speed *= 1.15
        if self.speed > 5:
            self.speed = 5

    def decelerate(self):
        self.speed *= 0.
        if self.speed < 0.5:
            self.speed = 0

    def to_dict(self):
        return {
            "id": self.id,
            "lane": self.lane,
            "speed": self.speed,
            "wainting_time": self.wainting_time,
            "x": self.x,
            "y": self.y,
            "hasPassed": self.hasPassed
        }
