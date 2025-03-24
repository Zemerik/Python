# Multi-level inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.doors = num_doors

class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_size):
        super().__init__(make, model, doors)
        self.battery = battery_size

# Usage
tesla = ElectricCar("Tesla", "Model S", 4, 100)
print(f"{tesla.make} {tesla.model} has {tesla.battery}kWh battery")