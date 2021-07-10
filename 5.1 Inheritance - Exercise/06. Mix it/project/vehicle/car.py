from project.vehicle.vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel ):
        super().__init__(available_seats)
        self.fuel_tank  = fuel_tank 
        self.fuel_consumption = fuel_consumption 
        self.__fuel = fuel 

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, needed_fuel):
        if needed_fuel - self.__fuel < self.fuel_tank:
            self.__fuel = needed_fuel
        else:
            self.__fuel = self.fuel_tank    
            

    def drive(self, distance): 
        if self.__fuel >= distance * self.fuel_consumption:
            self.__fuel -= distance * self.fuel_consumption
            return 'We\'ve enjoyed the travel!'


    def refuel(self, liters):
        result = self.get_capacity(self.fuel_tank, self.__fuel + liters)
        if not isinstance(result, str):
            self.__fuel += liters
        return self.fuel


          
