def get_primes(ints):
    for num in ints:
        if num == 2:
            yield num
        if num > 2:
            if not num % 2 == 0:
                yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
