class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.letter_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            if self.letter_counter == len(self.sequence):
                self.letter_counter = 0
            self.counter += 1
            curr_letter = self.letter_counter
            self.letter_counter += 1
            return self.sequence[curr_letter]
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')