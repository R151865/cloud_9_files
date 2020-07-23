import pytest
from truck import Truck


# unload
def test_unload_when_load_amount_greater_than_having_amount_then_cargo_weight_should_be_zero_only(truck1):

    # Arrage
    truck = truck1
    unload_amount = 30
    present_cargo_weight = 0
    current_speed = 0

    # Act
    truck.unload(unload_amount)

    # Arrage
    truck.unload(unload_amount)
    truck.unload(unload_amount)

    assert truck.current_speed == current_speed
    assert truck.load_weight == present_cargo_weight


@pytest.mark.parametrize(
    """max_speed, acceleration, tyre_friction, max_cargo_weight,
       cargo_weight, current_speed""", [
           (10, 1, 1, 10, 1, 1),
           (1, 10, 1, 10, 3, 1),
           (1, 5, 1, 13, 5, 1)
           ])
def test_unload_when_truck_engine_started_and_current_speed_is_not_zero_print_message(
        capsys, current_speed, max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction, max_cargo_weight=max_cargo_weight)
    cannot_load_during_motion_message = 'Cannot unload cargo during motion\n'
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.unload(cargo_weight)

    # Assert
    print_statement = capsys.readouterr()

    assert truck.is_engine_started is True
    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_during_motion_message


@pytest.mark.parametrize(
    'max_cargo_weight, load_amount, unload_amout, present_load_weight', [
        (10, 5, 3, 4),
        (30, 10, 9, 2)
        ])
def test_unload_when_truck_is_in_rest_condition_unloaded(
        max_cargo_weight, load_amount, unload_amout, present_load_weight):

    # Arrange
    max_speed = 1
    acceleration = 1
    tyre_friction = 1

    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    current_speed = 0
    truck.load(load_amount)
    truck.load(load_amount)

    # Act
    truck.unload(unload_amout)

    # Assert
    truck.unload(unload_amout)

    assert truck.current_speed == current_speed
    assert truck.load_weight == present_load_weight


@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (30, 10, 1, 30, -1),
        (1, 1, 1, 1, 0),
        (1, 1, 1, 1, -5)
        ])
def test_unload_when_invalid_cargo_weight_raise_value_error(
        max_speed, acceleration, tyre_friction, max_cargo_weight,
        cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    error_message_for_max_cargo_weight = 'Invalid value for cargo_weight'

    # Act
    with pytest.raises(Exception) as error:
        truck.unload(cargo_weight)

    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight
