import pytest
from car import Car


# Task-2
def test_start_engine_is_engine_started_return_true(car):

    # Arrange

    # Act
    car.start_engine()

    # Assert
    assert car.is_engine_started is True


def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(car):

    # Arrange
    intial_current_speed_of_car = 0

    # Act
    car.start_engine()

    # Assert
    assert car.is_engine_started is True
    assert car.current_speed == intial_current_speed_of_car


# Task 3
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction,current_speed", [
        (30, 10, 3, 20),
        (10, 5, 5, 10),
        (10, 6, 5, 10)
    ])
def test_start_engine_when_engine_started_and_accelerated_display_car_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrange
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()

    # Act
    car.accelerate()

    # Assert
    car.accelerate()

    assert car.is_engine_started is True
    assert car.current_speed == current_speed

def test_stop_engine_when_current_speed_is_not_zero_and_engine_stopped_suddenly_then_current_speed_should_be_not_zero(car):

    # Arrage
    car.start_engine()
    car.accelerate()
    current_speed_after_engine_stopped = 10

    # Act
    car.stop_engine()

    # Assert
    assert car.is_engine_started is False
    assert car.current_speed == current_speed_after_engine_stopped


def test_start_engine_when_multiple_engine_starts_and_stops_but_current_speed_should_not_be_zero(car):

    # Arrange
    car.start_engine()
    car.accelerate()
    car.stop_engine()
    current_speed_after_all = 20

    # Act
    car.start_engine()

    # Assert
    car.accelerate()

    assert car.current_speed == current_speed_after_all

# Task 7
def test_stop_engine_is_engine_started_return_false(car):

    # Arrange
    car.start_engine()

    # Act
    car.stop_engine()

    # Assert
    assert car.is_engine_started is False
