import pytest
from truck import Truck


def test_start_engine_when_multiple_engine_starts_and_stops_and_accelerates_but_current_should_not_be_zero(truck):

    # Arrange
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()
    current_speed_after_all = 20

    # Act
    truck.start_engine()
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed_after_all


# Task-2
def test_start_engine_is_engine_started_return_true(truck):

    # Arrange

    # Act
    truck.start_engine()

    # Assert
    assert truck.is_engine_started is True


def test_start_engine_when_intially_is_at_rest_and_current_speed_zero(truck):

    # Arrange
    intial_current_speed_of_truck = 0

    # Act
    truck.start_engine()

    # Assert
    assert truck.is_engine_started is True
    assert truck.current_speed == intial_current_speed_of_truck


# Task 3
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed, max_cargo_weight", [
        (30, 10, 3, 20, 1),
        (10, 5, 5, 10, 10),
        (10, 6, 5, 10, 100)
        ])
def test_start_engine_whether_displaying_current_speed_after_engine_started_and_accelerated(
        max_cargo_weight, max_speed, acceleration, tyre_friction, current_speed):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()

    # Act
    truck.accelerate()

    # Assert
    truck.accelerate()

    assert truck.is_engine_started is True
    assert truck.current_speed == current_speed


def test_stop_engine_when_current_speed_is_not_zero_and_engine_stopped_suddenly_but_current_speed_should_be_not_zero(truck):

    # Arrage
    truck.start_engine()
    truck.accelerate()
    current_speed_after_engine_stopped = 10

    # Act
    truck.stop_engine()

    # Assert
    assert truck.is_engine_started is False
    assert truck.current_speed == current_speed_after_engine_stopped


# Task 7
def test_stop_engine_is_engine_started_return_false(truck):

    # Arrange
    truck.start_engine()

    # Act
    truck.stop_engine()

    # Assert
    assert truck.is_engine_started is False
