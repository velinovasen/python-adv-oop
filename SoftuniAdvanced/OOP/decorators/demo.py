def cache(func):
    def wrapper(*args):
        if args in wrapper.log:
            return wrapper.log[args[0]]
        else:
            rv = func(*args)
            wrapper.log[args[0]] = rv

            return rv
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)
print(fibonacci.log)