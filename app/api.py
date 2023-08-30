import logging
from typing import Optional

import database
import schemas
import sensors
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DbSession

LOG = logging.getLogger("uvicorn.error")
routes = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@routes.get(
    "/sensors",
    status_code=200,
    response_model=schemas.ResponseListSensors,
    response_model_exclude_unset=True,
)
async def get_sensors(db: DbSession = Depends(get_db)):
    sensor_list = sensors.list_sensors_in_db(db=db)
    return {"items": sensor_list}


@routes.get("/sensors/{sensor_id}", status_code=200)
async def get_sensor(
    sensor_id: int,
    db: DbSession = Depends(get_db),
):
    sensor = sensors.get_sensor_in_db(sensor_id=sensor_id, db=db)
    return sensor


@routes.post("/sensors", status_code=201)
async def post_sensor(
    sensor_create: Optional[schemas.SensorCreate] = None,
    db: DbSession = Depends(get_db),
):
    sensor = sensors.add_sensor_to_db(sensor_create, db=db)
    return f"/sensors/{sensor['id']}"
