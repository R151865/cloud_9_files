from unittest.mock import patch
from is_weekend import is_weekend_using_get_current_day,is_weekend

"""
@patch('get_current_day.get_current_day')
def test_is_weekend_using_get_current_day_on_weekend(get_current_day_mock):
    get_current_day_mock.return_value=6
    
    result = is_weekend_using_get_current_day()
    
    assert result is True


@patch('get_current_day.get_current_day')
def test_is_weekend_using_get_current(a):
    a.return_value=1
    
    result = is_weekend_using_get_current_day()
    
    assert result is False
"""
from kalendar import MyCalendar
@patch.object(MyCalendar, 'get_current_day', return_value=5)
def test_weekend(get_current_day):
    from is_weekend import is_weekend
    result = is_weekend()
        
    assert result is False