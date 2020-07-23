def is_weekend_using_calendar(calendar_obj):
    day_as_number = calendar_obj.get_current_day()
    return day_as_number in [6, 7]


def is_weekend_using_get_current_day():
    from get_current_day import get_current_day
    day_as_number = get_current_day()
    return day_as_number in [6, 7]

def is_weekend():
    from kalendar import MyCalendar
    a=MyCalendar()
    day_as_number=a.get_current_day()
    #day_as_number = get_current_day()
    return day_as_number in [6, 7]
