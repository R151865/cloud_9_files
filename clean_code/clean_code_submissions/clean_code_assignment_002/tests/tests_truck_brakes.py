import pytest
from truck import Truck


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed", [
        (30, 10, 5, 5),
        (40, 2, 1, 1),
        (40, 30, 10, 20)
        ])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrage
    max_cargo_weight = 1
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.is_engine_started is True
    assert truck.current_speed == current_speed


def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(truck):

    # Arrange
    current_speed = 0

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.is_engine_started is False
    assert truck.current_speed == current_speed


def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(truck):

    # Arrange
    truck.start_engine()
    truck.accelerate()
    current_speed_should_be_zero = 0

    # Act
    truck.apply_brakes()

    # assert
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()
    truck.apply_brakes()

    assert truck.current_speed == current_speed_should_be_zero


def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_current_speed(truck):

    # Arrange
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    current_speed = 7

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.is_engine_started is False
    assert truck.current_speed == current_speed
