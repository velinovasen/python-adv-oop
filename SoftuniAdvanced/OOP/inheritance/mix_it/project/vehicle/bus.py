from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):

    def __init__(self, available_seats, ticket_price):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.ticket_sold = 0

    def get_ticket(self, tickets_count):
        mixin_result = self.get_capacity(self.available_seats, tickets_count)
        if isinstance(mixin_result, int):
            self.ticket_sold += tickets_count
            self.available_seats -= tickets_count
            return self.ticket_sold
        return mixin_result

    def get_total_profit(self):
        profit = self.ticket_price * self.ticket_sold
        return profit
