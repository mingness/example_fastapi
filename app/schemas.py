from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class SensorBase(BaseModel):
    sensor_id: str
    user_id: int


class Sensor(SensorBase):
    id: int = Field(primary_key=True)
    date_created: datetime


class ResponseListSensors(BaseModel):
    items: List[Sensor]
