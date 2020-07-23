import pytest
from car import Car


# Task-1 Creating car
def test_creating_multiple_car_instances_with_valid_details():

    # Arrange
    max_speed_1 = 30
    acceleration_1 = 12
    tyre_friction_1 = 11
    color_1 = 'Blue'

    max_speed_2 = 330
    acceleration_2 = 50
    tyre_friction_2 = 30
    color_2 = 'White'

    # Act
    car_1 = Car(color=color_1, max_speed=max_speed_1, acceleration=acceleration_1,
                tyre_friction=tyre_friction_1)
    car_2 = Car(color=color_2, max_speed=max_speed_2, acceleration=acceleration_2,
                tyre_friction=tyre_friction_2)

    # Assert
    assert car_1.color == color_1
    assert car_1.max_speed == max_speed_1
    assert car_1.tyre_friction == tyre_friction_1
    assert car_1.acceleration == acceleration_1
    assert car_2.color == color_2
    assert car_2.max_speed == max_speed_2
    assert car_2.tyre_friction == tyre_friction_2
    assert car_2.acceleration == acceleration_2


@pytest.mark.parametrize(
    """max_speed, acceleration, tyre_friction, color""", [
        (50, 5, 3, 'Blue'),
        (10, 2, 1, 'Red'),
        (100, 20, 19, 'Blue'),
        (100, 50, 1, 'White')
        ])
def test_create_car_when_valid_details_given_create_car(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    current_speed = 0

    # Act
    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    # arrange
    assert car.color == color
    assert car.max_speed == max_speed
    assert car.current_speed == current_speed
    assert car.acceleration == acceleration
    assert car.tyre_friction == tyre_friction


def test_create_car_when_color_not_given_return_default_color_blue():

    # Arrange
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    default_car_color_is_blue = 'Blue'

    # Act
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    # Assert
    assert car.color == default_car_color_is_blue


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (-1, 10, 3),
        (0, 3, 10)
        ])
def test_init_function_invalid_max_speed_raise_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_max_speed = 'Invalid value for max_speed'

    # Act
    with pytest.raises(ValueError) as error:
        Car(max_speed=max_speed, acceleration=acceleration,
            tyre_friction=tyre_friction)

    # Assert
    assert str(error.value) == invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_create_car():

    # Arrange
    max_speed = 1
    acceleration = 1
    tyre_friction = 1

    # Act
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    # Assert
    assert car.max_speed == max_speed


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (30, -1, 3),
        (40, 0, 10)
        ])
def test_init_function_invalid_acceleration_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_acceleration = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as error:
        Car(max_speed=max_speed, acceleration=acceleration,
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
        Car(max_speed=max_speed, acceleration=acceleration,
            tyre_friction=tyre_friction)

    # Assert
    assert str(error.value) == invalid_value_for_tyre_friction
