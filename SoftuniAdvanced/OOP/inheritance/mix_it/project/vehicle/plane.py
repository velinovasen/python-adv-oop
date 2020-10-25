from project.vehicle.vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self, available_seats, rows, seats_per_row):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    def buy_tickets(self, row_number, tickets_count):
        if row_number > self.rows:
            return f"There is no row {row_number} in the plane!"
        if row_number not in self.seats_available:
            self.seats_available[row_number] = self.seats_per_row
        mixin_result = self.get_capacity(self.seats_available[row_number], tickets_count)
        if isinstance(mixin_result, int):
            self.seats_available[row_number] -= tickets_count
            self.available_seats -= tickets_count
            return tickets_count
        return f"Not enough tickets on row {row_number}!"

