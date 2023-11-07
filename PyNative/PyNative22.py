class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __repr__(self):
        return f"Vehicle name: {self.name} \nVehicle Max Speed: {self.max_speed} mph \nVehicle Mileage: {self.mileage} mpg"


class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
print(bus)