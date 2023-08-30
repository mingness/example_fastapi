import logging

import schemas
from fastapi import APIRouter

LOG = logging.getLogger("uvicorn.error")
routes = APIRouter()


@routes.get("/sensors", response_model=schemas.ResponseListSensors, status_code=200)
async def get_sensors():
    sensor_list = []
    return {"items": sensor_list}
