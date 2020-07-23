
#abhands on db hit and how much time  taken to executes the given function

from django.db import connection
import time
import datetime
def decorators(func):
    
    def wrapper(*args, **kwargs):
        print('DateTime: {}'.format(datetime.datetime.now()))
        print('Function: {}'.format(func))
        print('Adress: {}'.format(id(func)))
        print('Args: {}'.format(args))
        print('Kwargs: {}'.format(kwargs))

        bef_time=time.time()
        result = func(*args,**kwargs)
        aft_time=time.time()
        
        print('No.of db hits: {}'.format(len(connection.queries)))
        print('Amount of Time: {}'.format(aft_time-bef_time))
        print()
        print('Result: {}'.format(result))

        return result

    return wrapper