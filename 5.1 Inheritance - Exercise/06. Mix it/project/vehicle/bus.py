from project.vehicle.vehicle import Vehicle
from project.capacity_mixin import CapacityMixin

class Bus(Vehicle, CapacityMixin):
    def __init__(self, available_seats , ticket_price, tickets_sold = 0):
        super().__init__(available_seats) 
        self.ticket_price = ticket_price
        self.tickets_sold = tickets_sold

    def get_ticket(self, tickets_count):
        result = self.get_capacity(self.available_seats, tickets_count)
        if not isinstance(result, str):
            self.available_seats -= tickets_count
            self.tickets_sold += tickets_count
        return result

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price