class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(int(value))
        return f"value is not a float"

    @classmethod
    def from_roman(cls, value):
        pass

    @classmethod
    def from_string(cls, value):
        pass

    def add(self, integer):
        return self.value + integer


first_num = Integer(10)
print(Integer.from_float(2.6))