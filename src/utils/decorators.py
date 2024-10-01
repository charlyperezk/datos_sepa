import time
import logging


def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f"Function {func.__name__} took {round(end_time - start_time, 3)} seconds to execute")
        return result
    return wrapper