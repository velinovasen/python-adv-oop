class dictionary_iter:
    def __init__(self, dic):
        self.dic = dic
        self.counter = 0
        self.keys = [x for x in self.dic.keys()]
        self.values = [x for x in self.dic.values()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dic):
            temp_idx = self.counter
            self.counter += 1
            return self.keys[temp_idx], self.values[temp_idx]
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

