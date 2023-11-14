class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2 

    def add(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Num2 is 0")
        return self.num1 / self.num2
    
    def exp(self):
        return self.num1 ** self.num2
    


calculator = Calculator(0,6)

print(calculator.add())
print(calculator.divide())
print(calculator.multiply())
print(calculator.exp())