from database import Base
from sqlalchemy import Column, DateTime, Integer, Text


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    device_id = Column(Text, index=True)
    # user_id = Column(Integer, index=True)  # TODO add user table
    datetime_created = Column(DateTime, index=True)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
