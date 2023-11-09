class Vehicle:

    def __init__(self, name, max_speed, mileage, color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


print(Car("BMW", 250, 25))