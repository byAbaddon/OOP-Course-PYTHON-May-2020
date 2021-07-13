from abc import ABC, abstractmethod 

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.aircondition = 0.9

    def drive(self, distance):
        fuel_cost  = distance * (self.fuel_consumption + self.aircondition) 
        if self.fuel_quantity >= fuel_cost:
            self.fuel_quantity -= fuel_cost


    def refuel(self, fuel):
        self.fuel_quantity += fuel



class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.aircondition  = 1.6
        self.lost_fuel = 0.95

    def drive(self, distance):
        fuel_cost  = distance * (self.fuel_consumption + self.aircondition) 
        if self.fuel_quantity >= fuel_cost:
            self.fuel_quantity -= fuel_cost


    def refuel(self, fuel):
        self.fuel_quantity +=  (fuel * self.lost_fuel)



