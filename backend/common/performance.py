import time
from functools import wraps


def measure_time(operation_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            operation_name_to_use = operation_name or func.__name__
            print(f"Execution time for '{operation_name_to_use}': {execution_time} seconds")
            return result

        return wrapper

    return decorator
