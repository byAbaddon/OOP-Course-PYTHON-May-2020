class Room:
    guests = 0
    is_taken = False
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def take_room(self, people):
        if not self.is_taken and self.capacity >= people:
            self.guests += people
            self.is_taken = True
        else:        
            return f'Room number {self.number} cannot be taken'

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:    
            return f'Room number {self.number} is not taken'
