import numpy as np
from matplotlib import pyplot as plt 
import math
import sympy as sym
from matplotlib.patches import Rectangle
from stackfunctionality import Stack
class GraphingCalculator:
    '''This is the graphing calculator class. It has the following methods:

        basic_calculator(user_input)- Performs basic calculations such as addition, subtraction, multiplication, division, 
                                      raising a number to a power, basic trigonometry 
        
        calculus_calculator(method, function)- Performs basic calculus operations such as derivatives, indefinite and definite integrals
                                               and limits
        
        graphing(function, plot_range)- Graphs functions over a certain interval using matplotlib
     
        geometry_graphin(user_input)- Graphs basic shapes using matplotlib
        
        statistics(data)- Performs basic statistics on a user defined data set

        stat_plot(data1, data2=None, plot='scatter')- Plots statistical plots, if a second data set is not input by the user,
                                                      the default is a histogram but if two data sets are provided then a scatter plot 
                                                      is created.
                                                      
        factorial(n)- computes the factorial of a number recursively

        sum_number(number)- computes the sum of all the numbers that precede the number you want to compute the sum of
        
        fib(n)- computes the fibonnaci number of a given number recursively
        '''
    def __init__(self):
        self.range = np.zeros(1)
        self.cache = {}
        self.memory = Stack()
    def basic_calculator(self, user_input):
            try:
            #Implements raising a number to a power
                if "**" in user_input:
                    x, z = user_input.split("**")
                    if x == 'ans':
                        x = self.memory.get_last()
                        z = float(z)
                    elif z == 'ans':
                        x = float(x)
                        z = self.memory.get_last()
                    else:
                        x = float(x)
                        z = float(z)
                    ans = x ** z
                    self.memory.add(ans)
                    return ans

        # Implements the square root of a number
                elif "sqrt" in user_input or "square root" in user_input:
                    x = None
                    if "sqrt" in user_input:
                        x = user_input.split("sqrt")[-1].strip()
                    elif "square root" in user_input:
                        x = user_input.split("square root")[-1].strip()

                    if x:
                        if x == 'ans':
                            x = self.memory.get_last()
                        else:
                            x = float(x)

                        ans = math.sqrt(x)
                        self.memory.add(ans)
                        return ans
                elif "trig" in user_input:
                    
                    angle_value = float(input("What angle do you want to use? (in radians): "))
                    trigonometric_function = input("What trigonometric operation would you like to perform? (sin, cos, tan): ")

                    if trigonometric_function == "sin":
                        result = sym.sin(angle_value)
                        self.memory.add(result)
                        return result

                    elif trigonometric_function == "cos":
                        result = sym.cos(angle_value)
                        self.memory.add(result)
                        return result

                    elif trigonometric_function == "tan":
                        result = sym.tan(angle_value)
                        self.memory.add(result)
                        return result

                #Implements all other mathematical operations
                elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
                    x, y, z = user_input.split(" ")
                    if x == 'ans':
                        x = self.memory.get_last()
                        z = float(z)
                    elif z == 'ans':
                        z = self.memory.get_last()
                        x = float(x)
                    else:
                        x = float(x)
                        z = float(z)

                    if y == "+":
                        ans = x + z
                        self.memory.add(ans)
                        return ans
                    
                    elif y == "-":
                        ans = x - z
                        self.memory.add(ans)
                        return ans
                    
                    elif y == "*":
                        ans = x * z
                        self.memory.add(ans)
                        return ans
                    
                    elif y == "/":
                        ans = x / z
                        self.memory.add(ans)
                        return ans
                    
            except ValueError:
                print("That is not a valid input")
            except ZeroDivisionError:
                print("Cannot divide by zero, please input a nonzero number")
            

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
    def graphing(self, function1, plot_range, function2=None):
        x = sym.symbols('x')
        expr1 = sym.sympify(function1)
        
        if function2:
            expr2 = sym.sympify(function2)
        
        start, stop = eval(plot_range)
        self.range = np.linspace(start, stop, 200)

        f = sym.lambdify(x, expr1, modules=["numpy"])
        y1_values = f(self.range)

        plt.plot(self.range, y1_values, 'b', label=function1)

        if function2:
            g = sym.lambdify(x, expr2, modules=["numpy"])
            y2_values = g(self.range)
            plt.plot(self.range, y2_values, 'r', label=function2)
            plt.legend()

            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('Graph of ' + function1 + ' and ' + function2)
        else:
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('Graph of ' + function1)

        plt.show()
            

    def geometry_graphing(self, user_input):
        if user_input == 'circle':
            ax = plt.axes()
            radius = float(int(input("What is the radius?: ")))
            theta = np.linspace(0, 2 * np.pi, 10000)
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)


            plt.plot(x, y)

            ax.set_title(f"$x^2 + y^2 = {radius}$")
            ax.set_xlabel("x")
            ax.set_ylabel("y")

            ax.grid()
            ax.axhline(0, color = "black")
            ax.axvline(0, color = "black")
            ax.set_aspect("equal")

            plt.show()

        elif user_input == 'square' or user_input == 'rectangle':
            length = float(input("What is the length?: "))
            width = float(input("What is the width?: "))
            fig, ax = plt.subplots()

            if user_input == 'square':
                # For a square, width and length are equal
                ax.add_patch(Rectangle((0, 0), width, width, angle=0))
                ax.set_title(f"Square with side length = {width}")
            else:
                ax.add_patch(Rectangle((0, 0), length, width, angle=0))
                ax.set_title(f"Rectangle with length = {length} and width = {width}")

            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid()
            ax.axhline(0, color="black")
            ax.axvline(0, color="black")
            ax.set_aspect("equal")
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

    def stat_plot(self, data1, data2=None, plot='scatter'):
        data1_array = np.array([float(x) for x in data1.split()])
        if data2:
            data2_array = np.array([float(x) for x in data2.split()])
        else:
            data2_array = None

        if plot == "scatter":
            if data2_array is not None:
                if len(data1_array) == len(data2_array):
                    plt.scatter(data1_array, data2_array)
                    plt.xlabel('Data 1')
                    plt.ylabel('Data 2')
                    plt.title('Scatter Plot')
                    plt.show()
                else:
                    print("Both datasets must have the same number of elements for a scatter plot.")
            else:
                print("Please provide two datasets for a scatter plot.")

        elif plot == "histogram":
            if data2_array is None:
                plt.hist(data1_array, bins='auto', color='blue', alpha=0.7)
                plt.xlabel('Values')
                plt.ylabel('Frequency')
                plt.title('Histogram for Data 1')
                plt.show()
            else:
                print("Cannot perform a histogram with two datasets. Please provide only one dataset.")
    def factorial(self, n):
        try:
            n = int(n)
            if n == 0 or n == 1:
                return 1
            else:
                return n * self.factorial(n-1)
        except ValueError:
            return "That is not a valid input, please input a number."
    def sum_number(self, number):
        try:
            number = int(number)
            if number == 0:
                return 0
            else:
                return number + self.sum_number(number-1)
        except ValueError:
            return "That is not a valid input, please input a number."
    def fib(self, n):
        try:
            n = int(n)
            if n == 0 or n == 1:
                return 1
            if n in self.cache:
                return self.cache[n]
            result =  self.fib(n-1) + self.fib(n-2)
            self.cache[n] = result             
            return result
        except ValueError:
            return "That is not a valid input, please input a number."
    


#Example implementation of graphing calculator class
def main():
    calculator = GraphingCalculator()
    while True:
        user_input = input("What would you like the calculator to do? ")
        if "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input or "**" in user_input or ("sqrt" or "square root") in user_input:
                print(calculator.basic_calculator(user_input))

        elif user_input == "calculus":
            function = input("What is the function?: ")
            method = input("What would you like to do to the function? (Derivative, Integration, Limit): ")
            print(calculator.calculus_calculator(method, function))

        elif user_input == "graphing":
            function1 = input("What is the function?: ")
            plot_range = input("What is the interval?: ")
            check_for_second_function = input("Would you like to graph another function?: (y/n):")
            if check_for_second_function == 'y':
                function2 = input("What is the function?: ")
                print(calculator.graphing(function1, plot_range, function2))
            elif check_for_second_function == 'n':
                print(calculator.graphing(function1, plot_range))

        elif user_input == "stats":
            data = input("Please input your data here: ")
            print(calculator.statistics(data))

        elif user_input == "stat plot":
            data1 = input("Please input your data here: ")
            check_for_data2 = input("Would you like to add a second data set? (y/n) ")

            if check_for_data2 == 'y':
                data2 = input("Please input your data here: ")
                calculator.stat_plot(data1, data2)

            elif check_for_data2 == 'n':
                calculator.stat_plot(data1,'histogram')    

        elif user_input == "trig":
            print(calculator.basic_calculator(user_input))

        elif user_input == "recursion":
            number = input("Please input a number: ")
            recursive_input = input("Which recursive function would you like? (Factorial, Sum, Fibonnaci): ")

            if recursive_input == "factorial":
                print(calculator.factorial(number))

            elif recursive_input == "sum":
                print(calculator.sum_number(number))

            elif recursive_input == "fib":
                print(calculator.fib(number))

        elif user_input == 'geometry plot':
            shape = input("What shape would you like?: ")
            calculator.geometry_graphing(shape)

        elif user_input in ["done", "exit"]:
            break

if __name__ == "__main__":
    main()
        