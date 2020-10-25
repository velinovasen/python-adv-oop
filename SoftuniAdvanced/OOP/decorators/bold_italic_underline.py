from functools import wraps


def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tok = func(*args, **kwargs)
        return f"<b>{tok}</b>"
    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tok = func(*args, **kwargs)
        return f"<i>{tok}</i>"

    return wrapper


def make_underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tok = func(*args, **kwargs)
        return f"<u>{tok}</u>"

    return wrapper



@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))