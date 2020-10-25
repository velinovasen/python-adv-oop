from functools import wraps


def tags(param):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tok = func(*args, **kwargs)
            return f"<{param}>{tok}</{param}>"

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))