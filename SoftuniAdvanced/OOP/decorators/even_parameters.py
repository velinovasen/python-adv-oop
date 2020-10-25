from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tok = [x for x in args if not isinstance(x, int)]
        if tok:
            return f'Please use only even numbers!'
        tokens = [x for x in args if x % 2 != 0]
        if tokens:
            return f'Please use only even numbers!'
        token = func(*args, **kwargs)
        return token

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))