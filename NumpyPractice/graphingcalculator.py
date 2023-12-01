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
                elif "trig" in user_input:
                    
                    angle_value = float(input("What angle do you want to use? (in radians): "))
                    trigonometric_function = input("What trigonometric operation would you like to perform? (sin, cos, tan): ")

                    if trigonometric_function == "sin":
                        result = sym.sin(angle_value)
                        return result

                    elif trigonometric_function == "cos":
                        result = sym.cos(angle_value)
                        return result

                    elif trigonometric_function == "tan":
                        result = sym.tan(angle_value)
                        return result

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
            start, stop= eval(plot_range)
            self.range = np.linspace(start, stop, 200)

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

    def statistics(self, data):
        try:
            
            data_array = np.array([float(x) for x in data.split()])
            
            # Calculate mean, variance, std deviation, and median using NumPy
            mean = np.mean(data_array)
            variance = np.var(data_array)
            std_dev = np.std(data_array)
            median = np.median(data_array)
            maximum = np.max(data_array)
            minimum = np.min(data_array)
            # Create a dictionary to store the calculated statistics
            statistics_dict = {
                'Mean': mean,
                'Variance': variance,
                'Standard Deviation': std_dev,
                'Minimum': minimum,
                'Median': median,
                'Maximum': maximum
            }
            
            return statistics_dict
            
        except ValueError:
            return "Invalid input. Please provide a space-separated list of numerical values."

    def stat_plot(self, data1, data2, plot):
        data1_array = np.array([float(x) for x in data1.split()])
        data2_array = np.array([float(x) for x in data2.split()])
        if plot == "scatter":
            plt.scatter(data1_array, data2_array)
            plt.show()
        elif plot == "histogram":
            plt.hist(data1_array, data2_array)
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
            print(calculator.graphing(function, plot_range))

        elif user_input == "stats":
            data = input("Please input your data here: ")
            print(calculator.statistics(data))

        elif user_input == "stat plot":
            data1 = input("Please input your data here: ")
            data2 = input("Please input your data here: ")
            plot = input("What type of plot would you like? (Scatter/Histogram): ")
            calculator.stat_plot(data1, data2,plot)
        elif user_input == "trig":
            print(calculator.basic_calculator(user_input))

        elif user_input in ["done", "exit"]:
            break

if __name__ == "__main__":
    main()
        