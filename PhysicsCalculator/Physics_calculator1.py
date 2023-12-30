import math
import numpy as np
from graphingcalculatorfunctionality import GraphingCalculator 

class PhysicsCalculator(GraphingCalculator):
    def __init__(self):
        super().__init__()
        self.g = 9.81

    def kinematics(self, t1=None, t2=None, x1=None, x2=None, a=None, V_0=None, V = None):
        if t1 is not None and t2 is not None:
            if t2 < t1:
                return "Time cannot be negative."

        if V is not None and V_0 is not None:
            if V_0 > 3e8 or V > 3e8:
                return "Speed cannot exceed the speed of light."

        if t1 is None and t2 is None:
            if V is None and V_0 is not None:
                if None in (a, x1, x2):
                    return "Insufficient parameters for calculation."
                V = math.sqrt((V_0 ** 2) + (2 * a * (x2 - x1)))
                self.memory.add(V)
                return f"V = {V} m/s"

            elif V_0 is None and V is not None:
                if None in (a, x1, x2):
                    return "Insufficient parameters for calculation."
                V_0 = math.sqrt((V**2) - (2 * a * (x2 - x1)))
                self.memory.add(V_0)
                return f"V_0 = {V_0} m/s"

            elif a is not None and V_0 is not None and x1 is not None and x2 is not None and V is not None:
                delta_t = (V - V_0) / a
                self.memory.add(delta_t)
                return f"Δt = {delta_t} s"

            elif V_0 is not None and V is not None and x1 is not None and x2 is not None and a is None:
                delta_x = (V**2 - V_0**2) / (2 * (x2 - x1))
                self.memory.add(delta_x)
                return f"Δx = {delta_x} m"
            
        elif x1 is None and x2 is None:
            if V is None and V_0 is not None:
                if None in (a, t1, t2):
                    return "Insufficient parameters for calculation."
                V = V_0 + a * (t2 - t1)
                self.memory.add(V)
                return f"V = {V} m/s"
            elif V is not None and V_0 is None:
                if None in (a, t1, t2):
                    return "Insufficient parameters for calculation."
                V_0 = V - a * (t2 - t1)
                self.memory.add(V_0)
                return f"V_0 = {V_0} m/s"
            elif t1 is None and  t2 is None:
                if None in (a, V, V_0):
                    return "Insufficient parameters for calculation."
                delta_t = (V - V_0) / a
                return f"Δt = {delta_t} s"
            elif t1 is None and  t2 is None and V is None:
                if None in (a, x2, x1, V_0):
                    return "Insufficient parameters for calculation."
                delta_t1 = ((-1* V_0) + math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
                delta_t2 = ((-1* V_0) - math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
                if delta_t1 > 0:
                    self.memory.add(delta_t1)
                    return f"Δt = {delta_t1} s"
                elif delta_t2 > 0:
                    self.memory.add(delta_t2)
                    return f"Δt = {delta_t2} s"
            elif t1 is None and  t2 is None and V_0 is None:
                if None in (a, x2, x1, V):
                    return "Insufficient parameters for calculation."
                delta_t1 = ((-1* V) + math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
                delta_t2 = ((-1* V) - math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
                if delta_t1 > 0:
                    self.memory.add(delta_t1)
                    return f"Δt = {delta_t1} s"
                elif delta_t2 > 0:
                    self.memory.add(delta_t2)
                    return f"Δt = {delta_t2} s"
        elif a == 0 and V_0 is None and V is None:
            if None in (x1, x2, t2, t1):
                return "Insufficient parameters for calculation."
            V = (x2 - x1) / (t2 - t1)
            self.memory.add(V)
            return f"V = {V} m/s"
        
    def calculus_kinematics(self, function, quantity, function_rep):
        if quantity == 'velocity':
            if function_rep == 'position':
                velocity = self.calculus_calculator("derivative", function)
                return velocity
            elif function_rep == 'acceleration':
                velocity = self.calculus_calculator("integration", function)
                return velocity
            
        elif quantity == 'acceleration':
            if function_rep == 'velocity':
                acceleration = self.calculus_calculator("derivative", function)
                return acceleration
            elif function_rep == 'displacement':
                velocity = self.calculus_calculator("derivative", function)
                acceleration = self.calculus_calculator("derivative", velocity)

        elif quantity == 'displacement':
            if function_rep == 'velocity':
                displacement = self.calculus_calculator("integration", function)
                return displacement
            elif function_rep == 'acceleration':
                velocity = self.calculus_calculator("integration", function)
                displacement = self.calculus_calculator("integration", velocity)

    def forces(self, user_input):
            #This implements the computation of an unknown mass or acceleration of the system of blocks 
            #(depending on the input parameters) through the pulley method
            if user_input == 'pulley':
                try:
                    acceleration = input("Please input a value for acceleration or 'none': ")
                    a = float(acceleration) if acceleration.lower() != 'none' else None
                except ValueError:
                    print("Please input a numerical value or 'none'.")

                masses_right = []
                masses_left = []
                print("Please input the masses on the right of the pulley.")
                while True:
                    try:
                        mass_input_right = input("Please input the mass of an object or 'exit': ")
                        if mass_input_right.lower() == 'exit':
                            break
                        mass = float(mass_input_right)
                        masses_right.append(mass)
                    except ValueError:
                        print("Please input a numerical value.")
                print("Please input the masses on the left of the pulley.")
                while True:
                    try:
                        mass_input_left = input("Please input the mass of an object or 'exit': ")
                        if mass_input_left.lower() == 'exit':
                            break
                        mass = float(mass_input_left)
                        masses_left.append(mass)
                    except ValueError:
                        print("Please input a numerical value.")
                
                return self.massless_pulley(masses_left, masses_right, a)

            elif user_input == 'inclinded plane':

                try:
                    mass = input("Please give the mass of the object or 'none': ")
                    m = float(mass) if mass.lower != 'none' else None
                except ValueError:
                    return "Please input a numerical value for the mass."
                
                try:
                    acceleration = input("Please input a value for acceleration or 'none': ")
                    a = float(acceleration) if acceleration.lower() != 'none' else None
                except ValueError:
                    print("Please input a numerical value or 'none'.")
                
                try:
                    angle = input("Please input a value for the angle: ")
                    theta = math.radians(float(angle)) 
                except ValueError:
                    print("Please input a numerical value for the angle.")

                friction = input("Is there friction? (y/n): ")
                if friction == 'y':
                    try:
                        mu = float(input("Please give the coefficient of friction of the object and the plane: "))
                    except ValueError:
                        return "Please input a value less than 1 but greater than 0 for the coefficient of friction."
                elif friction == 'n':
                    mu = None

                tension = input("Is there tension? (y/n): ")
                if tension == 'y':
                    try:
                        T = float(input("Please give the tension of the rope: "))
                    except ValueError:
                        return "Please input a value less than 1 but greater than 0 for the coefficient of friction."
                elif tension == 'n':
                    T = None
                
                return self.inclinded_plane(m,theta, acceleration, mu, T)


    def massless_pulley(self, masses_left, masses_right, acceleration=None):
        total_mass_left = sum(abs(mass) for mass in masses_left)
        total_mass_right = sum(abs(mass) for mass in masses_right)

        if total_mass_left == 0 or total_mass_right == 0:
            return "No masses provided on one side."

        net_force_left = sum(masses_left) * self.g
        net_force_right = sum(masses_right) * self.g

        if acceleration is None:
            acceleration = (net_force_right - net_force_left) / (total_mass_left + total_mass_right)
            tension_left = total_mass_left * (self.g + acceleration)
            tension_right = total_mass_right * (self.g - acceleration)
            self.memory.add([acceleration, tension_left, tension_right])
            return f"Acceleration = {acceleration} m/s^2, Tension on left side = {tension_left} N, Tension on right side = {tension_right} N"
        else:
            # Solve for unknown mass given acceleration
            if total_mass_left == 0:
                unknown_mass = (net_force_left + total_mass_right * self.g * (1 - acceleration / self.g)) / acceleration
            else:
                unknown_mass = (net_force_right + total_mass_left * self.g * (1 + acceleration / self.g)) / acceleration
            self.memory.add([acceleration, unknown_mass])
            return f"Acceleration = {acceleration} m/s^2, Unknown mass = {unknown_mass} kg"
        
    def inclinded_plane(self, theta, mass=None, acceleration=None, mu=None, tension=None):
        if mass is not None:
            y_component = mass * self.g * math.cos(theta)
            x_component = mass * self.g * math.sin(theta)
            if acceleration is None and mu is None and tension is None:
                a = x_component / mass
                self.memory.add(a)
                return f"Acceleration = {a} m/s^2"
            elif acceleration is None and mu is not None and tension is None:
                friction = y_component * mu 
                a = x_component - friction / mass
                self.memory.add(a)
                return f"Acceleration = {a} m/s^2"
            elif acceleration is None and mu is None and tension is not None:
                a = x_component - tension / mass
                self.memory.add(a)
                return f"Acceleration = {a} m/s^2"

        
PC = PhysicsCalculator()

# Test kinematics calculations
print(PC.kinematics(t1=0, t2=5, x1=None, x2=None, a=7, V_0=0, V=None))
# Provide specific values for x1 and x2 to trigger a calculation
print(PC.kinematics(t1=0, t2=5, x1=0, x2=100, a=None, V_0=0, V=None))
# Test a case where insufficient parameters are provided
print(PC.kinematics(t1=None, t2=None, x1=None, x2=None, a=None, V_0=None, V=None))
# Test the speed of light check
print(PC.kinematics(t1=None, t2=None, x1=0, x2=100, a=9.81, V_0=0, V=2.5e8))

# Test calculus kinematics
# Example usage (assuming a function and its representation are defined)
some_function = "x**3 + 2*x**2 + 5*x + 3"
print(PC.calculus_kinematics(function=some_function, quantity='velocity', function_rep='position'))

# Test forces calculations
# Test the pulley method
#print(PC.forces('pulley'))
# Test the inclined plane method
print(PC.forces('inclinded plane'))
