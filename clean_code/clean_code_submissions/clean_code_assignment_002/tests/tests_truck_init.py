import pytest
from truck import Truck


def test_creating_multiple_truck_instances_with_valid_details():

    # Arrange
    max_speed_1 = 30
    acceleration_1 = 12
    tyre_friction_1 = 11
    color_1 = 'Blue'
    max_cargo_weight_1 = 100

    max_speed_2 = 330
    acceleration_2 = 50
    tyre_friction_2 = 30
    color_2 = 'White'
    max_cargo_weight_2 = 150

    # Act
    truck_1 = Truck(max_cargo_weight=max_cargo_weight_1,
                    color=color_1,
                    max_speed=max_speed_1,
                    acceleration=acceleration_1,
                    tyre_friction=tyre_friction_1)
    truck_2 = Truck(max_cargo_weight=max_cargo_weight_2,
                    color=color_2,
                    max_speed=max_speed_2,
                    acceleration=acceleration_2,
                    tyre_friction=tyre_friction_2)

    # Assert
    assert truck_1.color == color_1
    assert truck_1.max_speed == max_speed_1
    assert truck_1.tyre_friction == tyre_friction_1
    assert truck_1.acceleration == acceleration_1
    assert truck_1.max_cargo_weight == max_cargo_weight_1

    assert truck_2.color == color_2
    assert truck_2.max_speed == max_speed_2
    assert truck_2.tyre_friction == tyre_friction_2
    assert truck_2.acceleration == acceleration_2
    assert truck_2.max_cargo_weight == max_cargo_weight_2


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, color, max_cargo_weight", [
        (50, 5, 3, 'Blue', 50),
        (10, 2, 1, 'Red', 100),
        (100, 20, 19, 'Blue', 10),
        (100, 50, 1, 'White', 5)
        ])
def test_create_truck_when_valid_details_given_by_checking_every_attribute(
        max_cargo_weight, color, max_speed, acceleration, tyre_friction):

    # Arrange

    # Act
    truck = Truck(color=color,
                  max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)

    # Arrange
    current_speed = 0

    assert truck.color == color
    assert truck.max_speed == max_speed
    assert truck.current_speed == current_speed
    assert truck.acceleration == acceleration
    assert truck.tyre_friction == tyre_friction
    assert truck.max_cargo_weight == max_cargo_weight


def test_create_truck_when_color_not_given_return_default_color_blue():

    # Arrange
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 200
    default_truck_color_is_blue = 'Blue'

    # Act
    truck = Truck(max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)

    # Assert
    assert truck.color == default_truck_color_is_blue


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction", [
        (-1, 10, 3),
        (0, 3, 10)
        ])
def test_init_function_when_invalid_max_speed_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_value_for_max_speed = 'Invalid value for max_speed'
    max_cargo_weight = 100

    # Act
    with pytest.raises(ValueError) as error:
        Truck(max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction,
              max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(error.value) == invalid_value_for_max_speed


def test_init_function_when_valid_max_speed_is_given_do_not_raise_error():

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
    assert truck.max_speed == max_speed


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction,", [
        (30, -1, 3),
        (40, 0, 10)
        ])
def test_init_function_when_invalid_acceleration_raise_value_error(
        max_speed, acceleration, tyre_friction):

    # Arrange
    max_cargo_weight = 10
    invalid_value_for_acceleration = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as error:
        Truck(max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction,
              max_cargo_weight=max_cargo_weight)

    # Assert
    assert str(error.value) == invalid_value_for_acceleration
