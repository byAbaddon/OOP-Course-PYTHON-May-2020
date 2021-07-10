from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self, fuel, horse_power):
        self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        consumption =  kilometers * self.fuel_consumption
        if self.fuel >= consumption:
            self.fuel -= consumption
            return self.fuel


