from SoftuniAdvanced.OOP.attributes_and_methods.movie_world.project.customer import Customer
from SoftuniAdvanced.OOP.attributes_and_methods.movie_world.project.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            return self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            return self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id]
        if customer[0]:
            customer = customer[0]
            cust_dvds = [x.id for x in customer.rented_dvds]
            if dvd_id in cust_dvds:
                cust_dv = [x.name for x in customer.rented_dvds if dvd_id == x.id]
                return f"{customer.name} has already rented {cust_dv[0]}"

        dvd = [x for x in self.dvds if x.id == dvd_id and x.is_rented == True]
        if dvd:
            return f"DVD is already rented"

        dvd_y_check = [x for x in self.dvds if x.id == dvd_id]
        if dvd_y_check:
            dvd_y_check = dvd_y_check[0]
        if dvd_y_check.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd_y_check.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd_y_check)
        dvd_y_check.is_rented = True
        return f"{customer.name} has successfully rented {dvd_y_check.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id]
        if customer:
            customer = customer[0]
        dvd = [x for x in customer.rented_dvds if dvd_id == x.id]
        if dvd:
            dvd = dvd[0]
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        token = ""
        for x in range(len(self.customers)):
            customer = self.customers[x]
            token += customer.__repr__() + "\n"
        for y in range(len(self.dvds)):
            dvd = self.dvds[y]
            token += dvd.__repr__() + "\n"
        return token

