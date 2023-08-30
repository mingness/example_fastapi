from datetime import datetime
from typing import List, Optional

import models
import schemas
from sqlalchemy.orm import Session


class CRUDSensors:
    def __init__(self, db: Session):
        self.model = models.Sensor
        self.db = db

    def get_by_id(self, sensor_id: int) -> Optional[models.Sensor]:
        return self.db.query(self.model).filter(self.model.id == sensor_id).first()

    def get_all(self) -> List:
        return self.db.query(self.model).all()

    def create(self, sensor: schemas.SensorCreate) -> Optional[models.Sensor]:
        if not sensor:
            return None

        query = self.model(**sensor.model_dump())
        query.datetime_created = datetime.now()

        self.db.add(query)
        self.db.commit()
        self.db.refresh(query)
        return query
