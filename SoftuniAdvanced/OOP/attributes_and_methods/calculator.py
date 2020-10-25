class Calculator:

    @staticmethod
    def add(*args):
        result = 0
        for x in args:
            result += x
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        nums = [int(x) for x in args]
        result = nums.pop(0)
        for x in nums:
            result /= x
        return result

    @staticmethod
    def subtract(*args):
        nums = [int(x) for x in args]
        result = nums.pop(0)
        for x in nums:
            result -= x
        return result

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))