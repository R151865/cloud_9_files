import pytest
from car import Car
from truck import Truck
from race_car import RaceCar


@pytest.fixture
def car():
    car_obj = Car(color='Blue',
                  max_speed=40,
                  acceleration=10,
                  tyre_friction=3)
    return car_obj


@pytest.fixture
def truck():
    color = 'Blue'
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 150

    truck_obj = Truck(color=color,
                      max_speed=max_speed,
                      acceleration=acceleration,
                      tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight)
    return truck_obj


@pytest.fixture
def truck1():
    max_speed = 30
    acceleration = 10
    tyre_friction = 5
    max_cargo_weight = 50

    truck_obj = Truck(max_speed=max_speed,
                      acceleration=acceleration,
                      tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight)
    return truck_obj


@pytest.fixture
def race_car1():
    max_speed = 50
    acceleration = 10
    tyre_friction = 5
    race_car_obj = RaceCar(max_speed=max_speed,
                           acceleration=acceleration,
                           tyre_friction=tyre_friction)

    return race_car_obj


@pytest.fixture
def race_car():
    color = 'Blue'
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    race_car_obj = RaceCar(color=color,
                           max_speed=max_speed,
                           acceleration=acceleration,
                           tyre_friction=tyre_friction)
    return race_car_obj
