import math
from graphingcalculatorfunctionality import GraphingCalculator 

class PhysicsCalculator(GraphingCalculator):
    def __init__(self):
        super().__init__()
        self.g = 9.81

    def kinematics(self, t1=None, t2=None, x1=None, x2=None, a=None, V_0=None, V = None):
        if t1!= None and t2 != None:
            if t2 < t1:
                raise ValueError("You can't have a negative time.")
        if V != None and V_0 != None:
            if V_0 > (3*(10**8)) or V > (3*(10**8)):
                raise ValueError("You can't have a speed faster than the speed of light.")
        if t1 == None and t2 == None and V == None:
            V = math.sqrt((V_0 ** 2) + (2 * a * (x2 - x1)))
            self.memory.add(V)
            return f"V = {V}"
        elif t1 == None and t2 == None and V_0 == None:
            V_0 = math.sqrt((V**2) - (2 * a * (x2-x1)))
            self.memory.add(V_0)
            return f"V_0 = {V_0}"
        elif t1 == None and t2 == None and a == None:
            a = (V**2 - V_0**2) / (2 * (x2 - x1))
            self.memory.add(a)
            return f"a = {a}"
        elif t1 == None and t2 == None and x1 == None and x2 == None:
            delta_x = (V**2 - V_0**2) / (2 * a)
            self.memory.add(delta_x)
            return f"Δx = {delta_x}"
        elif x1 == None and  x2 == None and V == None:
            V = V_0 + a * (t2 - t1)
            self.memory.add(V)
            return f"V = {V}"
        elif x1 == None and  x2 == None and V_0 == None:
            V_0 = V - a * (t2 - t1)
            self.memory.add(V_0)
            return f"V_0 = {V_0}"
        elif t1 == None and  t2 == None:
            delta_t = (V - V_0) / a
        elif t1 == None and  t2 == None and V == None:
            delta_t1 = ((-1* V_0) + math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
            delta_t2 = ((-1* V_0) - math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
            if delta_t1 > 0:
                self.memory.add(delta_t1)
                return f"Δt = {delta_t1}"
            elif delta_t2 > 0:
                self.memory.add(delta_t2)
                return f"Δt = {delta_t2}"
        elif t1 == None and  t2 == None and V_0 == None:
            delta_t1 = ((-1* V) + math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
            delta_t2 = ((-1* V) - math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2*(0.5 * a)
            if delta_t1 > 0:
                self.memory.add(delta_t1)
                return f"Δt = {delta_t1}"
            elif delta_t2 > 0:
                self.memory.add(delta_t2)
                return f"Δt = {delta_t2}"
        elif a == 0 and V_0 == None and V == None:
            V = (x2 - x1) / (t2 - t1)
            self.memory.add(V)
            return f"V = {V}"
        
    def forces(self, user_input):
        if user_input == 'pulley':
            try:
                acceleration = input("Please input a value for acceleration or none: ")
                if acceleration == 'none':
                    a = None
                else:
                    a = float(int(acceleration))
            except ValueError:
                print("Please input a numerical value or none.")
            masses_list = []
            while True:
                try:
                    masses_right = input("Please input the mass of the object or exit: ")
                    if masses_right == "exit":
                        break 
                    else:
                        masses_list.append(float(int(masses_right)))
                except ValueError:
                    print("Please input a numerical value.")
                    continue
            while True:
                try:
                    masses_left = input("Please input the mass of the object or exit: ")
                    if masses_left == "exit":
                        break 
                    else:
                        masses_list.append(-1 * float(int(masses_left)))
                except ValueError:
                    print("Please input a numerical value.")
                    continue
            self.pulley(masses_list, a)

    def pulley(self, masses_list, a=None):
        if a ==  None:
            total_mass = 0
            for mass in masses_list:
                total_mass += abs(mass)
            net_force = sum(masses_list) * self.g
            return f"Acceleration = {net_force / total_mass}"
        else:
            net_force_w_o_missing_block = sum(masses_list) * self.g
            masses_times_acceleration = sum(masses_list) * a
            return f"Unknown mass = {(net_force_w_o_missing_block - masses_times_acceleration) / (self.g + a)}"


        
PC = PhysicsCalculator()
print(PC.kinematics(t1=0, t2=5, x1=None, x2=None, a=7, V_0=0, V = None))
