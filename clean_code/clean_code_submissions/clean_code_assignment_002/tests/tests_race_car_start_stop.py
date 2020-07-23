import pytest
from race_car import RaceCar


# Task-2
def test_start_engine_is_engine_started_return_true(race_car):

    # Arrange

    # Act
    race_car.start_engine()

    # Assert
    assert race_car.is_engine_started is True


def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(race_car):

    # Arrange
    intial_current_speed_of_race_car = 0

    # Act
    race_car.start_engine()

    # Assert
    assert race_car.is_engine_started is True
    assert race_car.current_speed == intial_current_speed_of_race_car


# Task 3
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed", [
        (30, 10, 3, 20),
        (10, 5, 5, 10),
        (10, 6, 5, 10)
        ])
def test_start_engine_when_engine_started_and_accelerated_by_checking_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrange
    race_car = RaceCar(max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()

    # Act
    race_car.accelerate()

    # Assert
    race_car.accelerate()

    assert race_car.is_engine_started is True
    assert race_car.current_speed == current_speed


def test_stop_engine_when_current_speed_is_not_zero_stop_engine_suddenly_return_current_speed(
        race_car):

    # Arrage
    race_car.start_engine()
    race_car.accelerate()
    current_speed_after_engine_stopped = 10

    # Act
    race_car.stop_engine()

    # Assert
    assert race_car.is_engine_started is False
    assert race_car.current_speed == current_speed_after_engine_stopped


def test_start_engine_with_multiple_engine_starts_and_stops_but_current_speed_should_not_be_zero(race_car):

    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.stop_engine()
    current_speed_after_all = 20

    # Act
    race_car.start_engine()

    # Assert
    race_car.accelerate()

    assert race_car.current_speed == current_speed_after_all


def test_stop_engine_is_engine_started_return_false(race_car):

    # Arrange
    race_car.start_engine()

    # Act
    race_car.stop_engine()

    # Assert
    assert race_car.is_engine_started is False
