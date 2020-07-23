import pytest
from race_car import RaceCar


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed", [
        (30, 10, 5, 5),
        (40, 2, 1, 1),
        (40, 30, 10, 20)
        ])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrage
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.is_engine_started is True
    assert race_car.current_speed == current_speed


def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(
        race_car):

    # Arrange
    current_speed = 0

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.is_engine_started is False
    assert race_car.current_speed == current_speed


def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(race_car):

    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    current_speed_should_be_zero = 0

    # Act
    race_car.apply_brakes()

    # assert
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()

    assert race_car.current_speed == current_speed_should_be_zero


def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_checking_current_speed_is_correct_or_not(race_car):

    # Arrange
    race_car.start_engine()
    race_car.accelerate()
    race_car.stop_engine()
    current_speed = 10

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.is_engine_started is False
    assert race_car.current_speed == current_speed
