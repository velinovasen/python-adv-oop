from functools import wraps

def type_check(type):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if type.__name__ == args[0].__class__.__name__:
                tok = func(*args, **kwargs)
                return tok
            else:
                return f"Bad Type"

        return wrapper

    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))