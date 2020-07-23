import pytest
from truck import Truck


# Task 4
@pytest.mark.parametrize(
    """max_speed, acceleration, tyre_friction, current_speed,
       max_cargo_weight""", [
           (30, 29, 3, 29, 11), (30, 31, 1, 30, 1), (30, 30, 30, 30, 10)
           ])
def test_accelerate_when_engine_started_return_current_speed(
        max_cargo_weight, max_speed, acceleration, tyre_friction,
        current_speed):

    # Arrange
    truck_current_speed_after_acceleration = current_speed
    truck = Truck(
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )
    truck.start_engine()

    # Act
    truck.accelerate()

    # Assert
    assert truck.is_engine_started is True
    assert truck.current_speed == truck_current_speed_after_acceleration


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, 29, 3),
        (50, 35, 1),
        (10, 5, 3)
        ])
def test_accelerate_above_max_speed_and_current_speed_is_equal_to_max_speed_only(
        max_speed, acceleration, tyre_friction):

    # Arrange
    max_cargo_weight = 100
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck_max_speed = max_speed
    truck.start_engine()

    # Act
    truck.accelerate()

    # Assert
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    assert truck.is_engine_started is True
    assert truck.current_speed == truck_max_speed


def test_accelerate_when_truck_is_not_started_print_message(
        truck, capsys):

    # Arrange
    message_to_start_engine_to_accelerate = 'Start the engine to accelerate\n'

    # Act
    truck.accelerate()

    # Assert
    output = capsys.readouterr()

    assert truck.is_engine_started is False
    assert output.out == message_to_start_engine_to_accelerate
