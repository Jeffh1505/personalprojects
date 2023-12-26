import math
from graphingcalculatorfunctionality import GraphingCalculator 

class PhysicsCalculator(GraphingCalculator):
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
            return V
        elif t1 == None and t2 == None and V_0 == None:
            V_0 = math.sqrt((V**2) - (2 * a * (x2-x1)))
            self.memory.add(V_0)
            return V_0
        elif t1 == None and t2 == None and a == None:
            a = (V**2 - V_0**2) / (2 * (x2 - x1))
            self.memory.add(a)
            return a
        elif t1 == None and t2 == None and x1 == None and x2 == None:
            delta_x = (V**2 - V_0**2) / (2 * a)
            self.memory.add(delta_x)
            return delta_x
        elif x1 == None and  x2 == None and V == None:
            V = V_0 + a * (t2 - t1)
            self.memory.add(V)
            return V
        elif x1 == None and  x2 == None and V_0 == None:
            V_0 = V - a * (t2 - t1)
            self.memory.add(V_0)
            return V_0
        elif t1 == None and  t2 == None:
            delta_t = (V - V_0) / a
        elif t1 == None and  t2 == None and V == None:
            delta_t1 = ((-1* V_0) + math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2(0.5 * a)
            delta_t2 = ((-1* V_0) - math.sqrt(V_0**2 - 4 * 0.5 * a * (x2-x1))) / 2(0.5 * a)
            if delta_t1 > 0:
                self.memory.add(delta_t1)
                return delta_t1
            elif delta_t2 > 0:
                self.memory.add(delta_t2)
                return delta_t2
        elif t1 == None and  t2 == None and V_0 == None:
            delta_t1 = ((-1* V) + math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2(0.5 * a)
            delta_t2 = ((-1* V) - math.sqrt(V**2 - 4 * 0.5 * a * (x2-x1))) / 2(0.5 * a)
            if delta_t1 > 0:
                self.memory.add(delta_t1)
                return delta_t1
            elif delta_t2 > 0:
                self.memory.add(delta_t2)
                return delta_t2
        elif a == 0:
            V = (x2 - x1) / (t2 - t1)
        

        
PC = PhysicsCalculator()
print(PC.kinematics(t1=0, t2=5, x1=None, x2=None, a=7, V_0=0, V = None))
