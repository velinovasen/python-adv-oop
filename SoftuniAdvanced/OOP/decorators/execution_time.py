from functools import wraps
from time import perf_counter


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        tok = func(*args, **kwargs)
        end_time = perf_counter()
        return end_time - start_time
    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))