import pytest
from truck import Truck


# Task 5
def test_sound_horn_when_truck_engine_started_and_print_beep_beep(
        truck, capsys):

    # Arrange
    truck.start_engine()
    honk_honk_sound = 'Honk Honk\n'

    # Act
    truck.sound_horn()
    output = capsys.readouterr()

    # Assert
    assert truck.is_engine_started is True
    assert output.out == honk_honk_sound


def test_sound_horn_when_truck_engine_stopped_return_string(
        truck, capsys):

    # Arrange
    start_engine_to_sound_horn_string = 'Start the engine to sound_horn\n'

    # Act
    truck.sound_horn()
    output = capsys.readouterr()

    # Assert
    assert truck.is_engine_started is False
    assert output.out == start_engine_to_sound_horn_string


# max cargo weight
@pytest.mark.parametrize(
    'max_cargo_weight', [
        (0),
        (-1),
        (-2)
        ])
def test_init_function_when_invalid_max_cargo_weight_raise_value_error(
        max_cargo_weight):

    # Arrange
    max_speed = 30
    acceleration = 10
    tyre_friction = 5
    error_message_for_max_cargo_weight = 'Invalid value for max_cargo_weight'

    # Act
    with pytest.raises(Exception) as error:
        Truck(max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction,
              max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(error.value) == error_message_for_max_cargo_weight


def test_init_function_when_valid_max_cargo_weight_do_not_raise_value_error():

    # Arrange
    max_speed = 1
    acceleration = 1
    tyre_friction = 1
    max_cargo_weight = 1

    # Act
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)

    # Assert
    assert truck.max_cargo_weight == max_cargo_weight


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, 10, -1),
        (40, 10, 0)
        ])
def test_init_function_invalid_tyre_friction_raise_value_error_(
        max_speed, acceleration, tyre_friction):

    # Arrange
    max_cargo_weight = 1
    invalid_value_for_tyre_friction = 'Invalid value for tyre_friction'

    # Act
    with pytest.raises(ValueError) as error:
        Truck(max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction,
              max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(error.value) == invalid_value_for_tyre_friction


def test_sound_horn_when_engine_is_stop_print_message(
        capsys, truck):

    # Arrange
    start_engine_to_sound_horn_string = 'Start the engine to sound_horn\n'

    # Act
    truck.sound_horn()

    # Assert
    output = capsys.readouterr()

    assert truck.is_engine_started is False
    assert output.out == start_engine_to_sound_horn_string
