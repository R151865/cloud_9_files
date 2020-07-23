import pytest

@pytest.fixture
def car():
    from .car import Car
    car_obj=Car(color='Blue',max_speed=40,acceleration=10,tyre_friction=3)
    return car_obj
