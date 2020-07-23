import pytest
from car import Car


# Task 4
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction,current_speed", [
        (30, 29, 3, 29),
        (30, 31, 1, 30),
        (30, 30, 30, 30)
        ])
def test_accelerate_when_engine_started_return_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrange
    car_current_speed_after_acceleration = current_speed
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()

    # Act
    car.accelerate()

    # Assert
    assert car.is_engine_started is True
    assert car.current_speed == car_current_speed_after_acceleration


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, 29, 3),
        (50, 35, 1),
        (10, 5, 3)
    ])
def test_accelerate_above_max_speed_and_current_speed_should_be_max_speed(
        max_speed, acceleration, tyre_friction):

    # Arrange
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car_max_speed = max_speed
    car.start_engine()

    # Act
    car.accelerate()

    # Assert
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    assert car.is_engine_started is True
    assert car.current_speed == car_max_speed


def test_accelerate_when_car_is_not_started_print_message(car, capsys):

    # Arrange
    message_to_start_engine_to_accelerate = 'Start the engine to accelerate\n'

    # Act
    car.accelerate()

    # Assert
    output = capsys.readouterr()

    assert car.is_engine_started is False
    assert output.out == message_to_start_engine_to_accelerate
