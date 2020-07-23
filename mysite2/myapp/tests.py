#from django.test import TestCase
import pytest


def test_acceleration_car(car):
    car.start_engine()
    car.accelerate()
    
    assert car.current_speed==10
