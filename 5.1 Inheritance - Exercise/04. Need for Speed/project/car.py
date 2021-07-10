from project.vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel, horse_power):
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        consumption =  kilometers * self.fuel_consumption
        if self.fuel >= consumption:
            self.fuel -= consumption
            return self.fuel
