from typing import Optional
import aioredis
from fastapi import FastAPI
from mqttcfg import mqtt

app = FastAPI()
redis = aioredis.from_url("redis://redis")
mqtt.init_app(app)

@app.get("/status")
def read_status():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/set/{key}")
async def set_key(key: str, val: Optional[str] = ""):
    await redis.set(key, val)
    ret_val = await redis.get(key)
    return {key:ret_val}

@app.get("/get/{key}")
async def get_key(key: str):
    ret_val = await redis.get(key)
    return {key:ret_val}

@app.get("/game/status")
async def get_status():
    return {}

@app.get("/timer/start")
async def timer_start():
    return

@app.get("/mqtt/{topic}")
async def mqtt_send(topic: str, body: Optional[str] = ""):
    mqtt.publish(topic, body)
    return

"""
MQTT:
/d/torch/1
/d/chest/

/game/status
/game/torch/1
/game/torch/2
/game/chest
"""