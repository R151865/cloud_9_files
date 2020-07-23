import pytest


@pytest.fixture
def car():
    from car import Car
    car_obj = Car(
                  color='Blue',
                  max_speed=40,
                  acceleration=10,
                  tyre_friction=3
    )
    return car_obj

@pytest.fixture
def truck():
    from truck import Truck
    color = 'Blue'
    max_speed = 40
    acceleration = 10
    tyre_friction = 3
    max_cargo_weight = 150

    truck_obj = Truck(
                      color=color,
                      max_speed=max_speed,
                      acceleration=acceleration,
                      tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight
    )
    return truck_obj


@pytest.fixture
def truck1():
    from truck import Truck
    max_speed = 30
    acceleration = 10
    tyre_friction = 5
    max_cargo_weight = 50

    truck_obj = Truck(
                      max_speed=max_speed,
                      acceleration=acceleration,
                      tyre_friction=tyre_friction,
                      max_cargo_weight=max_cargo_weight
    )
    return truck_obj

@pytest.fixture
def race_car1():
    from race_car import RaceCar
    max_speed =50
    acceleration = 10
    tyre_friction = 5
    race_car_obj=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    return race_car_obj
    
@pytest.fixture
def race_car():
    from race_car import RaceCar
    color='Blue'
    max_speed=40
    acceleration=10
    tyre_friction=3
    race_car_obj=RaceCar(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    return race_car_obj

@pytest.fixture
def race_car1():
    from race_car import RaceCar
    max_speed =50
    acceleration = 10
    tyre_friction = 5
    race_car_obj=RaceCar(max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    return race_car_obj
    
@pytest.fixture
def race_car():
    from race_car import RaceCar
    color='Blue'
    max_speed=40
    acceleration=10
    tyre_friction=3
    race_car_obj=RaceCar(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    return race_car_obj
