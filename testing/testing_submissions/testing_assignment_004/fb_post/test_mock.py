
from django.test import TestCase
from freezegun import freeze_time
from fb_post.exceptions import InvalidUserException
import pytest

from fb_post.models import Party
from fb_post.mock_file import get_count_field_from_object
pytestmark=pytest.mark.django_db

#from requests.exceptions import TimeOut
from unittest.mock import patch,Mock



def get_stock_price(company_id):
    import requests
    import json
    #from requests.exceptions import TimeOut 
    try:
        response = requests.get(" http://www.mocky.io/v2/5eb664e831000057006999f3")
    except InvalidUserException:
        raise Exception('sulthan')
    except :
        return 10000
    return response.content
    result = json.loads(response.content)
 
    return result['unit_price_in_inr']


@patch('json.loads')
def test_stock_price(json_mock):
    
    json_mock.return_value={'unit_price_in_inr':100}
    
    # Arrange
    # Act
    result = get_stock_price(10)
    print(result)
    assert result ==1001






"""
class MyClass:
    def __init__(self, name, age):
        import uuid
        self.id = uuid.uuid4()
        self.name = name
        self.age = age

@patch('uuid.uuid4')
def test_init_myclass(uuid_mock):
    uuid_mock.return_value=0
    obj = MyClass('Sulthan', 20)
    
    assert obj.name == 'Sulthan'
    assert obj.age == 20
    assert obj.id == 0
"""

"""
import time
def get_epoch_time_stamp_as_str():
    return str(time.time())

@patch('time.time')
def test_get_epoch_time_stamp(time_mock):
    time_mock.return_value="Sulthan"

    value = get_epoch_time_stamp_as_str()
    assert value is "Sulthan"
"""