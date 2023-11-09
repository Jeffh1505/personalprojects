class Vehicle:

    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

    def __repr__(self):
        return f"Color: {self.color} \nVehicle name: {self.name} \nVehicle Max Speed: {self.max_speed} mph \nVehicle Mileage: {self.mileage} mpg"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


print(Car("BMW", 250, 25))