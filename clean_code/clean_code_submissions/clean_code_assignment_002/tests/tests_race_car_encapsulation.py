import pytest


# Task 8
def test_encapsulation_for_current_speed_when_assign_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_current_speed = "can't set attribute"
    value_assigning_to_private_variable = 0

    # Act
    with pytest.raises(Exception) as error:
        race_car.current_speed = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_current_speed


def test_encapsulation_for_acceleration_when_assign_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_acceleration = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        race_car.acceleration = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_acceleration


def test_encapsulation_for_color_when_assign_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_color = "can't set attribute"
    value_assigning_to_private_variable = 'Black'

    # Act
    with pytest.raises(Exception) as error:
        race_car.color = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_color


def test_encapsulation_for_tyre_friction_when_assign_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_tyre_friction = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        race_car.tyre_friction = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_tyre_friction


def test_encapsulation_for_max_speed_when_assign_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_max_speed = "can't set attribute"
    value_assigning_to_private_variable = 5

    # Act
    with pytest.raises(Exception) as error:
        race_car.max_speed = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_max_speed


def test_encapsulation_for_is_engine_started_raise_attribute_error(
        race_car):

    # Arrange
    value_error_message_to_is_engine_started = "can't set attribute"
    value_assigning_to_private_variable = False

    # Act
    with pytest.raises(Exception) as error:
        race_car.is_engine_started = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_is_engine_started


def test_encapsulation_of_nitro_when__assign_raise_attribute_error(
        race_car1):

    # Arrange
    race_car = race_car1
    value_error_message_to_is_nitro = "can't set attribute"
    value_assigning_to_private_variable = 1

    # Act
    with pytest.raises(Exception) as error:
        race_car.nitro = value_assigning_to_private_variable

    # Assert
    assert str(error.value) == value_error_message_to_is_nitro
