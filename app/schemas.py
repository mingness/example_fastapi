from typing import List, Optional

from pydantic import BaseModel, Field


class SensorBase(BaseModel):
    device_id: str


class SensorCreate(SensorBase):
    pass


class Sensor(SensorBase):
    id: int = Field(primary_key=True)
    date_created: Optional[str]


class ResponseListSensors(BaseModel):
    items: List
