
class Computation:
    def __init__(self) -> None:
        pass

    def factorial(self, number):
        if number <= 1:
            return 1
        else:
            return number * self.factorial(number-1)

    def sum_number(self, number):
        if number == 0:
            return 0
        else:
            return number + self.sum_number(number-1)
        


c = Computation()

print(c.factorial(4))
print(c.sum_number(5))
        


