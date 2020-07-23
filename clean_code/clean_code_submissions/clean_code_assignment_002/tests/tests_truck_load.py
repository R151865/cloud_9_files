import pytest
from truck import Truck


# cargo_weight
@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (30, 10, 1, 30, -1),
        (1, 1, 1, 1, 0),
        (1, 1, 1, 1, -2),
        (1, 1, 1, 1, -10)
        ])
def test_load_when_invalid_cargo_weight_raise_value_error(
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
        truck.load(cargo_weight)

    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight


# load
@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (30, 10, 1, 30, 1),
        (1, 1, 1, 1, 10),
        (1, 1, 1, 1, 1)
        ])
def test_load_when_truck_engine_started_and_in_motion_print_statement(
        capsys, max_speed, acceleration, tyre_friction, max_cargo_weight,
        cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.start_engine()
    truck.accelerate()
    cannot_load_during_motion_message = 'Cannot load cargo during motion\n'

    # Act
    truck.load(cargo_weight)

    # Assert
    print_statement = capsys.readouterr()

    assert truck.is_engine_started is True
    assert str(print_statement.out) == cannot_load_during_motion_message


# load when it is rest only
@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (1, 1, 1, 1, 1),
        (1, 1, 1, 10, 9)
        ])
def test_load_when_truck_is_in_rest_condition(
        max_speed, acceleration, tyre_friction,
        max_cargo_weight, cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck_present_load_weight = cargo_weight
    current_speed = 0

    # Act
    truck.load(cargo_weight)

    # Assert
    assert truck.current_speed == current_speed
    assert truck.load_weight == truck_present_load_weight


# test load within more than max_cargo_weight should raise print statement
@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (1, 1, 1, 1, 1),
        (1, 1, 1, 10, 9),
        (1, 1, 1, 13, 7)
        ])
def test_load_when_load_weight_more_than_max_cargo_weight_print_statement(
        capsys, max_speed, acceleration, tyre_friction, max_cargo_weight,
        cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    current_speed = 0
    cannot_load_cargo_more_than_max_limit = ('Cannot load cargo more '
                                             'than max limit: {}\n'
                                             .format(max_cargo_weight))

    # Act
    truck.load(cargo_weight)

    # Assert
    truck.load(cargo_weight)
    print_statement = capsys.readouterr()

    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_cargo_more_than_max_limit


def test_load_when_truck_engine_started_and_current_speed_is_zero(truck1):

    # Arrange
    truck = truck1
    current_speed = 0
    load_weight = 10
    present_truck_load_weight = 20
    truck.start_engine()

    # Act
    truck.load(load_weight)

    # Assert
    truck.load(load_weight)

    assert truck.is_engine_started is True
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_truck_load_weight


@pytest.mark.parametrize(
    """max_speed,
       acceleration,
       tyre_friction,
       max_cargo_weight,
       cargo_weight,
       current_speed""", [
           (10, 1, 1, 10, 1, 1),
           (1, 10, 1, 10, 3, 1),
           (1, 5, 1, 13, 5, 1)
           ])
def test_load_when_truck_engine_started_and_current_speed_is_not_zero_print_message(
        capsys, current_speed, max_speed, acceleration, tyre_friction,
        max_cargo_weight, cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    cannot_load_during_motion_message = 'Cannot load cargo during motion\n'
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.load(cargo_weight)

    # Assert
    print_statement = capsys.readouterr()

    assert truck.is_engine_started is True
    assert truck.current_speed == current_speed
    assert str(print_statement.out) == cannot_load_during_motion_message


def test_load_when_truck_engine_stopped_and_current_speed_is_zero(truck1):

    # Arrange
    truck = truck1
    current_speed = 0
    load_weight = 10
    present_truck_load_weight = 20
    truck.start_engine()
    truck.stop_engine()

    # Act
    truck.load(load_weight)

    # Assert
    truck.load(load_weight)

    assert truck.is_engine_started is False
    assert truck.current_speed == current_speed
    assert truck.load_weight == present_truck_load_weight


@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, max_cargo_weight, cargo_weight', [
        (1, 1, 1, 10, 1),
        (1, 1, 1, 10, 3),
        (1, 1, 1, 13, 5)
        ])
def test_load_when_truck_engine_stopped_and_current_speed_is_not_zero_print_message(
        capsys, max_speed, acceleration, tyre_friction, max_cargo_weight,
        cargo_weight):

    # Arrange
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    cannot_load_during_motion_message = 'Cannot load cargo during motion\n'
    truck.start_engine()
    truck.accelerate()
    truck.stop_engine()

    # Act
    truck.load(cargo_weight)

    # Assert
    print_statement = capsys.readouterr()

    assert truck.is_engine_started is False
    assert str(print_statement.out) == cannot_load_during_motion_message
