from functools import wraps


class cache:
    def __init__(self, func):
        self.log = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[0] in self.log:
            return self.log[args[0]]
        tok = self.func(*args, *kwargs)
        self.log[args[0]] = tok
        return tok


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(93)
print(fibonacci.log)