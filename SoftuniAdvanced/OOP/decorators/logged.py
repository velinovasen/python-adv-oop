from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = func(*args, **kwargs)
        return f"you called {func.__name__}({', '.join([str(x) for x in args])})\nit returned {token}"

    return wrapper




@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))