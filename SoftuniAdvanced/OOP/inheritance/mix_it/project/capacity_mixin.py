
class CapacityMixin:

    @staticmethod
    def get_capacity(capacity, amount):
        if capacity < amount:
            return f"Capacity reached!"
        return capacity - amount