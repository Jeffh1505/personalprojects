class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __repr__(self):
        return f"Vehicle Max Speed: {self.max_speed} mph \nVehicle Mileage: {self.mileage} mpg"




c = vehicle(250, 25)

print(c)