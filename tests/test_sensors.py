from unittest.mock import Mock, patch

import fixtures
from sqlalchemy.orm import Session as DbSession

import app.sensors as sensors


@patch("crud.CRUDSensors.get_all")
def test_list_sensors_in_db_empty(mock_crud_method):
    # arrange
    mock_crud_method.return_value = []
    expected = []
    # act
    actual = sensors.list_sensors_in_db(Mock(DbSession))
    # assert
    assert len(actual) == 0
    assert actual == expected


@patch("crud.CRUDSensors.get_all")
def test_list_sensors_in_db_one(mock_crud_method):
    # arrange
    mock_crud_method.return_value = [fixtures.row1]
    expected = [fixtures.row1_dict]
    # act
    actual = sensors.list_sensors_in_db(Mock(DbSession))
    # assert
    assert len(actual) == 1
    assert actual == expected


@patch("crud.CRUDSensors.get_all")
def test_list_sensors_in_db_three(mock_crud_method):
    # arrange
    mock_crud_method.return_value = [fixtures.row1, fixtures.row2, fixtures.row3]
    expected = [fixtures.row1_dict, fixtures.row2_dict, fixtures.row3_dict]
    # act
    actual = sensors.list_sensors_in_db(Mock(DbSession))
    # assert
    assert len(actual) == 3
    assert actual == expected


@patch("crud.CRUDSensors.get_by_id")
def test_get_sensor_in_db_empty(mock_crud_method):
    # arrange
    mock_crud_method.return_value = None
    expected = {}
    # act
    actual = sensors.get_sensor_in_db(1, Mock(DbSession))
    # assert
    assert actual == expected


@patch("crud.CRUDSensors.get_by_id")
def test_get_sensor_in_db_success(mock_crud_method):
    # arrange
    mock_crud_method.return_value = fixtures.row1
    expected = fixtures.row1_dict
    # act
    actual = sensors.get_sensor_in_db(1, Mock(DbSession))
    # assert
    assert actual == expected


@patch("crud.CRUDSensors.create")
def test_add_sensor_in_db_empty(mock_crud_method):
    # arrange
    mock_crud_method.return_value = None
    expected = {}
    # act
    actual = sensors.add_sensor_to_db(None, Mock(DbSession))
    # assert
    assert actual == expected


@patch("crud.CRUDSensors.create")
def test_add_sensor_in_db_success(mock_crud_method):
    # arrange
    mock_crud_method.return_value = fixtures.row1
    expected = fixtures.sensor_1.model_dump()
    expected.pop("datetime_created")
    # act
    actual = sensors.add_sensor_to_db(fixtures.sensor_create_1, Mock(DbSession))
    # assert
    actual.pop("datetime_created")
    assert actual == expected
