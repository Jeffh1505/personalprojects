class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def combine(self, other):
        return self.val() + other.val()
    def add(self, y):
        self.x += y
    def val(self):
        return self.x + self.y
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def val(self):
        return self.a * self.b
    def add(self,y):
        self.b += y
instance1 = A(1,3)
instance2 = B(2,2)
instance1.add(1)
instance2.add(3)
print(instance1.combine(instance2))