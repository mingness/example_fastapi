from typing import Dict, List

import crud
import schemas
from sqlalchemy.orm import Session as DbSession


def list_sensors_in_db(db: DbSession) -> List[Dict]:
    crud_sensor = crud.CRUDSensors(db=db)
    raw_list = crud_sensor.get_all()
    return [item.to_dict() for item in raw_list]


def get_sensor_in_db(sensor_id: int, db: DbSession) -> Dict:
    crud_sensor = crud.CRUDSensors(db=db)
    return crud_sensor.get_by_id(sensor_id).to_dict()


def add_sensor_to_db(sensor_create: schemas.SensorCreate, db: DbSession) -> Dict:
    crud_sensor = crud.CRUDSensors(db=db)
    return crud_sensor.create(sensor_create).to_dict()
