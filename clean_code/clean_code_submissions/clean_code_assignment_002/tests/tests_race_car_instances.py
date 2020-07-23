from race_car import RaceCar


# Task-1 Creating race_car
def test_creating_multiple_race_car_instances_with_valid_details():

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
    race_race_car_1 = RaceCar(color=color_1, max_speed=max_speed_1,
                              acceleration=acceleration_1,
                              tyre_friction=tyre_friction_1)
    race_race_car_2 = RaceCar(color=color_2, max_speed=max_speed_2,
                              acceleration=acceleration_2,
                              tyre_friction=tyre_friction_2)

    # Assert
    assert race_race_car_1.color == color_1
    assert race_race_car_1.max_speed == max_speed_1
    assert race_race_car_1.tyre_friction == tyre_friction_1
    assert race_race_car_1.acceleration == acceleration_1

    assert race_race_car_2.color == color_2
    assert race_race_car_2.max_speed == max_speed_2
    assert race_race_car_2.tyre_friction == tyre_friction_2
    assert race_race_car_2.acceleration == acceleration_2


def test_create_race_car_when_color_not_given_return_default_color_blue():

    # Arrange
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    default_race_car_color_is_blue = 'Blue'

    # Act
    race_car = RaceCar(max_speed=max_speed, acceleration=acceleration,
                       tyre_friction=tyre_friction)

    # Assert
    assert race_car.color == default_race_car_color_is_blue
