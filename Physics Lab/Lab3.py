import numpy as np
import matplotlib as plt 
ten_microfarad = [15, 10, 8,6,5,4.5, 4, 3, 2, 2, 2,1.5,1.25, 1, 1,1,1,1,0.8, 0.5, 0.5,0.4, 0.4, 0.3, 0.25,0.20,0.15,0.1,0.05,0.05,0.01,0.01, 0.01,0.01,0.01]
print(len(ten_microfarad))

def linearize(L: list):
    new_list = np.array(L)
    Linearized_list = np.log(new_list)
    return Linearized_list

print(linearize(ten_microfarad))

