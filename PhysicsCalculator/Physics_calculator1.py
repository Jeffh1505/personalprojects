import math
from graphingcalculatorfunctionality import GraphingCalculator 

class PhysicsCalculator(GraphingCalculator):
    def kinematics(self, t1=None, t2=None, x1=None, x2=None, a=None, V_0=None, V = None):
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
        
print(PhysicsCalculator.kinematics(t1=None, t2=None, x1=3, x2=7, a=5, V_0=0, V = None))
