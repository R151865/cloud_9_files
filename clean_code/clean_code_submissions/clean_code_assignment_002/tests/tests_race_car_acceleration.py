import pytest
from race_car import RaceCar


# Task 4
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed", [
        (30, 29, 3, 29),
        (30, 31, 1, 30),
        (30, 30, 30, 30)
        ])
def test_accelerate_when_engine_started_return_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrange
    race_car_current_speed_after_acceleration = current_speed
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.is_engine_started is True
    assert race_car.current_speed == race_car_current_speed_after_acceleration


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, 29, 3),
        (50, 35, 1),
        (10, 5, 3)
        ])
def test_accelerate_above_max_speed_and_current_speed_is_equal_to_max_speed_only(
        max_speed, acceleration, tyre_friction):

    # Arrange
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car_max_speed = max_speed
    race_car.start_engine()

    # Act
    race_car.accelerate()

    # Assert
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    assert race_car.is_engine_started is True
    assert race_car.current_speed == race_car_max_speed


def test_accelerate_when_race_car_is_not_started_print_message(
        race_car, capsys):

    # Arrange
    message_to_start_engine_to_accelerate = 'Start the engine to accelerate\n'

    # Act
    race_car.accelerate()

    # Assert
    output = capsys.readouterr()

    assert race_car.is_engine_started is False
    assert output.out == message_to_start_engine_to_accelerate
