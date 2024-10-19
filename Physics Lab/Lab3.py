import numpy as np
import matplotlib as plt 
ten_microfarad_charging = [15, 10, 8,6,5,4.5, 4, 3, 2, 2, 2,1.5,1.25, 1, 1,1,1,1,0.8, 0.5, 0.5,0.4, 0.4, 0.3, 0.25,0.20,0.15,0.1,0.05,0.05,0.01,0.01, 0.01,0.01,0.01]

twenty_microfarad_charging = [14, 10.25, 9.85, 9, 8, 7, 6, 5.75, 5.25, 5, 4.75, 4,3.95, 3.25, 3.05, 3, 2.85, 2.75,2.25, 2, 1.95, 1.85, 1.75, 1.65, 1.5, 1.45, 1.25, 1.05, 1.01,1.0,1.0, 1.0,1,1,1,]
print(len(twenty_microfarad_charging))
thirty_microfarad_charging = []

def linearize(L: list):
    new_list = np.array(L)
    Linearized_list = np.log(new_list)
    return Linearized_list



