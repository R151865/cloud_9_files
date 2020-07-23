import pytest
from race_car import RaceCar


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (-1, 10, 3),
        (0, 3, 10)
        ])
def test_init_function_invalid_max_speed_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_max_speed = 'Invalid value for max_speed'

    # Act
    with pytest.raises(ValueError) as error:
        RaceCar(max_speed=max_speed, acceleration=acceleration,
                tyre_friction=tyre_friction)

    # Assert
    assert str(error.value) == invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_do_not_raise_error():

    # Arrange
    max_speed = 1
    acceleration = 1
    tyre_friction = 1

    # Act
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert race_car.max_speed == max_speed


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, -1, 3),
        (40, 0, 10)]
        )
def test_init_function_invalid_acceleration_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_acceleration = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as error:
        RaceCar(max_speed=max_speed, acceleration=acceleration,
                tyre_friction=tyre_friction)

    # Assert
    assert str(error.value) == invalid_value_for_acceleration


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, 10, -1),
        (40, 10, 0)
        ])
def test_init_function_invalid_tyre_friction_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_tyre_friction = 'Invalid value for tyre_friction'

    # Act
    with pytest.raises(ValueError) as error:
        RaceCar(max_speed=max_speed, acceleration=acceleration,
                tyre_friction=tyre_friction)

    # Assert
    assert str(error.value) == invalid_value_for_tyre_friction
