import math

class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def area(self):
        area = math.pi * (self.r**2)
        return area
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.r
        return perimeter
    

circle = Circle(4)
print(circle.area())
print(circle.perimeter())