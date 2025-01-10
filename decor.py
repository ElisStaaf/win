import time
from functools import wraps
from typing import Callable, Any
from time import sleep


def retry(retries: int = 3, delay: float = 1) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    # Don't let the user use this decorator if they are high
    if retries < 1 or delay <= 0:
        raise ValueError('UnhandledException')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        print(f'Error: {repr(e)} -> Retrying...')
                        sleep(delay)  # Add a delay before running the next iteration

        return wrapper

    return decorator

def debug(func): # Debug mode, incredibly useful tool

    @wraps(func)

    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]

        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]

        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__}() returned {repr(value)}")

        return value
        
    return wrapper_debug