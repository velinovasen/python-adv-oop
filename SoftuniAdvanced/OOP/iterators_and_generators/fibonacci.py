def fibonacci():
    last_num = 0
    curr_num = 1
    while True:
        yield last_num
        last_num, curr_num = curr_num, last_num + curr_num


generator = fibonacci()
for i in range(5):
    print(next(generator))