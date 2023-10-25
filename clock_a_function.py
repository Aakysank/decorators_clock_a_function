import time
from functools import wraps
def decorator(fptr):
    @wraps(fptr)
    def wrapper(*args, **kwds):
        print(f'Measuring time taken to compute {len(args)} numbers')

        start_time = time.time()
        i = fptr(*args, **kwds)
        end_time = time.time()

        print(f'Time taken to average {len(args)} numbers is {end_time-start_time}')
        return i
    return wrapper


@decorator
def average(*args: int)->float:
    '''
    This function computes the average of any numbers

    Parameters : int or float 

    returns - float
    '''
    
    if len(args) == 0:
        return BaseException

    print(f'Average of the numbers is {sum(args)/len(args)}')
                    
