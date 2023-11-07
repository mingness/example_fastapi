import datetime
from unittest.mock import MagicMock

import app.schemas as schemas

sensor_create_1 = schemas.SensorCreate(
    device_id="device1",
)
sensor_1 = schemas.Sensor(
    id=1,
    device_id="device1",
    datetime_created=datetime.datetime.now().isoformat(),
)
sensor_create_2 = schemas.SensorCreate(
    device_id="device2",
)
sensor_2 = schemas.Sensor(
    id=2,
    device_id="device2",
    datetime_created=datetime.datetime.now().isoformat(),
)
sensor_create_3 = schemas.SensorCreate(
    device_id="device3",
)
sensor_3 = schemas.Sensor(
    id=3,
    device_id="device3",
    datetime_created=datetime.datetime.now().isoformat(),
)

row1_dict = dict(
    id=1,
    device_id="device1",
    datetime_created=datetime.datetime.now(),
)
row1 = MagicMock()
row1.to_dict.return_value = row1_dict

row2_dict = dict(
    id=2,
    device_id="device2",
    datetime_created=datetime.datetime.now(),
)
row2 = MagicMock()
row2.to_dict.return_value = row2_dict

row3_dict = dict(
    id=3,
    device_id="device3",
    datetime_created=datetime.datetime.now(),
)
row3 = MagicMock()
row3.to_dict.return_value = row3_dict
