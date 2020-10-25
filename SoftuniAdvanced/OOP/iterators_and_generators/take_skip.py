class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            temp_num = self.num
            self.counter += 1
            self.num += self.step
            if temp_num == 0:
                return 0
            return temp_num
        raise StopIteration()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

numbers = take_skip(2, 6)
for number in numbers:
    print(number)