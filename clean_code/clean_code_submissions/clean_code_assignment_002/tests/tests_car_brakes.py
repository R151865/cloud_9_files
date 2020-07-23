import pytest

# Task-5
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction,current_speed", [
        (30, 10, 5, 5),
        (40, 2, 1, 1),
        (40, 30, 10, 20)
        ])
def test_apply_brakes_when_engine_started_and_accelerated_return_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):

    # Arrage
    from car import Car
    car = Car(max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.is_engine_started is True
    assert car.current_speed == current_speed


def test_apply_brakes_when_engine_is_at_rest_and_not_started_then_current_speed_zero(car):

    # Arrange
    current_speed = 0

    # Act
    car.apply_brakes()

    # Assert
    assert car.is_engine_started is False
    assert car.current_speed == current_speed


def test_apply_brakes_with_multiple_times_but_current_speed_should_not_be_negative_value_but_it_should_be_zero_only(car):

    # Arrange
    car.start_engine()
    car.accelerate()
    current_speed_should_be_zero = 0

    # Act
    car.apply_brakes()

    # assert
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    assert car.current_speed == current_speed_should_be_zero


def test_apply_brakes_when_current_speed_is_some_value_and_engine_is_started_accelerated_stopped_and_current_speed(car):

    # Arrange
    car.start_engine()
    car.accelerate()
    car.stop_engine()
    current_speed = 7

    # Act
    car.apply_brakes()

    # Assert
    assert car.is_engine_started is False
    assert car.current_speed == current_speed
