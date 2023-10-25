import time
def decorator(fptr):
    def wrapper(*args):
        print(f'Measuring time taken to compute {len(args)} numbers')

        start_time = time.time()
        i = fptr(*args)
        end_time = time.time()

        print(f'Time taken to average {len(args)} numbers is {end_time-start_time}')
        return i
    return wrapper


@decorator
def average(*args: int)->float:
    if len(args) == 0:
        return BaseException

    print(f'Average of the numbers is {sum(args)/len(args)}')
                    
