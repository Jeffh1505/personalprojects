import numpy as np
from matplotlib import pyplot as plt 
import math
import sympy as sym

class GraphingCalculator:
    def __init__(self) -> None:
        self.range = np.zeros(1)
    def basic_calculator(self, user_input):
            try:
            #Implements raising a number to a power
                if "**" in user_input:
                    x, z = user_input.split("**")
                    x = float(x)
                    z = float(z)
                    return  x ** z
                
                #Implements the square root of a number
                elif "sqrt" in user_input or "square root" in user_input:
                    if "sqrt" in user_input:
                        x = float(user_input.split("sqrt")[1])
                    else:
                        x = float(user_input.split("square root")[1])

                    return math.sqrt(x)
                
                #Implements all other mathematical operations
                elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
                    x, y, z = user_input.split(" ")
                    x = float(x)
                    z = float(z)
                    if y == "+":
                        return x + z
                    elif y == "-":
                        return x - z
                    elif y == "*":
                        return x * z
                    elif y == "/":
                        return x / z
            except ValueError:
                print("That is not a valid input")
            

        #Performs calculus operations
    def calculus_calculator(self, method, function):
        x = sym.symbols('x')

        #Takes the derivative of a function
        if method.lower() == "derivative":
            derivative = sym.diff(function, x)
            return derivative
            
            #Takes the integral of a function
        elif method.lower() == "integration":
            check_for_limits = input("Would you like to add limits? (y/n): ").lower()
            if check_for_limits == 'y':
                upper_limit = input("What is the upper limit (or 'inf' for infinity)?: ").lower()
                lower_limit = input("What is the lower limit (or '-inf' for negative infinity)?: ").lower()
                    
                if upper_limit == 'inf':
                    upper_limit = sym.oo
                else:
                    upper_limit = float(upper_limit)
                    
                if lower_limit == '-inf':
                    lower_limit = -sym.oo
                else:
                    lower_limit = float(lower_limit)
                    
                definite_integral = sym.integrate(function, (x, lower_limit, upper_limit))
                return definite_integral
                
            elif check_for_limits == 'n':
                indefinite_integral = sym.integrate(function, x)
                return indefinite_integral

            else:
                return print("Invalid choice for limits. Please enter 'y' or 'n'.")
    def graphing(self, function, plot_range):
            # Generate a range of values using numpy linspace
            x = sym.symbols('x')

        # Convert the input function string into a SymPy expression
            expr = sym.sympify(function)

            # Generate a range of values using numpy linspace
            start, stop, num_points = eval(plot_range)
            self.range = np.linspace(start, stop, num_points)

            # Create a lambda function to evaluate the SymPy expression numerically
            f = sym.lambdify(x, expr, modules=["numpy"])

            # Evaluate the function for each value in the range
            y_values = f(self.range)

            # Plot the graph
            plt.plot(self.range, y_values)
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('Graph of ' + function)
            plt.show()

            

def main():
    calculator = GraphingCalculator()
    while True:
        user_input = input("What would you like the calculator to do? ")
        if "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input or "**" in user_input or ("sqrt" or "square root") in user_input:
                print(calculator.basic_calculator(user_input))

            #Implements calculus functionality
        elif user_input == "calculus":
            function = input("What is the function?: ")
            method = input("What would you like to do to the function? (Derivative, Integration, Limit): ")
            print(calculator.calculus_calculator(method, function))
        elif user_input == "graphing":
            function = input("What is the function?: ")
            plot_range = input("What is the interval?: ")
            calculator.graphing(function, plot_range)
        elif user_input in ["done", "exit"]:
            break

if __name__ == "__main__":
    main()
        