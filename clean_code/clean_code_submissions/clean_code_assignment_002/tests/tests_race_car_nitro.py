import pytest
from race_car import RaceCar


# test case to check wether nitro is zero or not when nitro become negative
def test_nitro_edge_condition_when_nitro_becomes_negative_but_should_return_zero():

    # Arrange
    max_speed = 20
    acceleration = 11
    tyre_friction = 9
    nitro_value_should_be_zero = 0
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    race_car.accelerate()

    assert race_car.nitro == nitro_value_should_be_zero


@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction', [
        (10, 10, 10),
        (1, 1, 1),
        (1, 10, 1)
        ])
def test_nitro_when_created_race_car_should_return_nitro_value_zero(
        max_speed, acceleration, tyre_friction):

    # Arrange
    nitro_value_should_be_zero = 0

    # Act
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert race_car.nitro == nitro_value_should_be_zero


@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, nitro_value', [
        (10, 10, 5, 10),
        (10, 1, 9, 0),
        (5, 3, 1, 10),
        (5, 10, 1, 20),
        (10, 1, 1, 0),
        (6, 5, 2, 10)
        ])
def test_nitro_on_applying_brakes_when_current_speed_less_than_equal_to_and_greater_than_half_of_max_speed(
        nitro_value, max_speed, acceleration, tyre_friction):

    # Arrage
    race_car = RaceCar(max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    race_car.apply_brakes()

    assert race_car.is_engine_started is True
    assert race_car.nitro == nitro_value


# test_nitro_whether_nitro_adding_or_not_to_acceleration_when_available
@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, current_speed, nitro_value', [
        (10, 10, 5, 10, 0),
        (20, 10, 10, 10, 0),
        (20, 11, 10, 16, 0)
        ])
def test_nitro_whether_nitro_adding_or_not_to_acceleration_when_available(
        nitro_value, current_speed, max_speed, acceleration, tyre_friction):

    # Arrage
    race_car = RaceCar(max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.is_engine_started is True
    assert race_car.nitro == nitro_value
    assert race_car.current_speed == current_speed


@pytest.mark.parametrize(
    'max_speed, acceleration, tyre_friction, nitro_value', [
        (50, 30, 1, 20),
        (20, 11, 1, 0),
        (20, 12, 1, 10),
        (20, 13, 1, 20)
        ])
def test_nitro_whether_is_it_reducing_or_not_when_accelerate(
        max_speed, acceleration, tyre_friction, nitro_value):

    # Arrage
    race_car = RaceCar(max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    race_car.start_engine()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.is_engine_started is True
    assert race_car.nitro == nitro_value


def test_nitro_whether_is_it_displaying_nitro_value(race_car1):

    # Arrage
    nitro_value = 20
    race_car = race_car1
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    race_car.apply_brakes()

    assert race_car.is_engine_started is True
    assert race_car.nitro == nitro_value
