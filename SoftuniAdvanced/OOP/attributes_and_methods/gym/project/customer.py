
class Customer:
    c_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        Customer.c_id += 1
        self.id = Customer.c_id

    @staticmethod
    def get_next_id():
        return Customer.c_id + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; " \
               f"Email: {self.email}"