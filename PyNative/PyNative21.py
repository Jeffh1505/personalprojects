class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __repr__(self) -> str:
        return f"Vehicle Max Speed: {self.max_speed} \nVehicle Mileage: {self.mileage}"




c = vehicle(25, 25)

print(c)