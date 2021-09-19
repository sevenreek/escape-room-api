from datetime import date, datetime, timedelta
from enum import Enum

class RoomTimer():
    class STATE(Enum):
        PAUSED = 0
        RUNNING = 1

    def __init__(self):
        self.created_on = datetime.now()
        self.state = RoomTimer.STATE.STOPPED
        self.seconds_left_from_resumed = 0
        self.time_resumed = None
    
    def start(self):
        if self.state == RoomTimer.STATE.RUNNING:
            pass
        elif self.state == RoomTimer.STATE.PAUSED:
            self.time_resumed = datetime.now()

    def pause(self):
        if self.time_resumed:
            self.seconds_left_from_resumed -= (datetime.now() - self.time_resumed).total_seconds()
        self.state = RoomTimer.STATE.PAUSED
    
    def set_duration(self, duration:int):
        self.seconds_left_from_resumed = duration

    def add_time(self, secs:int):
        self.seconds_left_from_resumed += secs
    
    def remaining(self):
        if self.state == RoomTimer.STATE.RUNNING:
            return self.seconds_left_from_resumed - (datetime.now() - self.time_resumed).total_seconds()
        elif self.state == RoomTimer.STATE.PAUSED:
            return self.seconds_left_from_resumed

    

class Room():
    def __init__(self, name:str):
        self.name = name
        self.timer = RoomTimer()
        self.devices = []
        self.current_stage = 0
        