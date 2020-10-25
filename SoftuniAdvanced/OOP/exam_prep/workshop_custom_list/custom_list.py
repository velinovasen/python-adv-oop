import copy


class CustomListTypeException(Exception):
    pass


class CustomListIndexException(Exception):
    pass


class CustomListSumException(Exception):
    pass


class CustomList:
    def __init__(self, *args):
        self.token = [el for el in args]

    def append(self, value):
        self.token += [value]
        return self.token

    def remove(self, index):
        try:
            result = self.token[index]
            del self.token[index]
            return result

        except IndexError:
            raise CustomListIndexException('No such index inside of list')

        except TypeError:
            raise CustomListTypeException('Input should be integer')

    def get(self, index):
        try:
            return self.token[index]

        except IndexError:
            raise CustomListIndexException('No such index inside of the list')

        except TypeError:
            raise CustomListTypeException('Input should be integer')

    def extend(self, iterable):
        self.token += list(iterable)
        return self.token

    def insert(self, index, value):
        self.token = self.token[:index] + [value] + self.token[index:]
        return self.token

    def pop(self):
        result = self.token[-1]
        self.token = self.token[:-1]
        return self.token

    def clear(self):
        self.token = []

    def index(self, value):
        pass

    def count(self, value):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass


l1 = CustomList(23, 'sddaz', 5)
print(l1.append(3))
print(l1.pop())