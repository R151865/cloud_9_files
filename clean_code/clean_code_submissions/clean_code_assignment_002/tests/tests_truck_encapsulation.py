import pytest


# Task 8
def test_encapsulation_for_current_speed_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_current_speed = "can't set attribute"
    value_assigning_to_private_variable = 0

    # Act
    with pytest.raises(Exception) as error:
        truck.current_speed = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_current_speed


def test_encapsulation_for_acceleration_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_acceleration = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        truck.acceleration = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_acceleration


def test_encapsulation_for_color_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_color = "can't set attribute"
    value_assigning_to_private_variable = 'Black'

    # Act
    with pytest.raises(Exception) as error:
        truck.color = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_color


def test_encapsulation_for_tyre_friction_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_tyre_friction = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        truck.tyre_friction = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_tyre_friction


def test_encapsulation_for_max_speed_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_max_speed = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        truck.max_speed = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_max_speed


def test_encapsulation_for_is_engine_started_raise_attribute_error(truck):

    # Arrange
    value_error_message_to_is_engine_started = "can't set attribute"
    value_assigning_to_private_variable = False

    # Act
    with pytest.raises(Exception) as error:
        truck.is_engine_started = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_is_engine_started


# encapsulation
def test_encapsulation_of_max_cargo_weight_raise_attribute_error(truck1):

    # Arrange
    truck = truck1
    value_error_message_to_is_max_cargo_weight = "can't set attribute"
    assigning_value_to_private_attribute = 1

    # Act
    with pytest.raises(Exception) as error:
        truck.max_cargo_weight = assigning_value_to_private_attribute

    # Assert
    assert str(error.value) == value_error_message_to_is_max_cargo_weight


def test_encapsulation_of_load_weight_raise_attribute_error(truck1):

    # Arrange
    truck = truck1
    value_error_message_to_is_load_weight = "can't set attribute"
    assigning_value_to_private_attribute = 1

    # Act
    with pytest.raises(Exception) as error:
        truck.max_cargo_weight = assigning_value_to_private_attribute

    # Assert
    assert str(error.value) == value_error_message_to_is_load_weight
