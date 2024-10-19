import numpy as np
import matplotlib as plt 
ten_microfarad_charging = [15, 10, 8,6,5,4.5, 4, 3, 2, 2, 2,1.5,1.25, 1, 1,1,1,1,0.8, 0.5, 0.5,0.4, 0.4, 0.3, 0.25,0.20,0.15,0.1,0.05,0.05,0.01,0.01, 0.01,0.01,0.01]

twenty_microfarad_charging = [14, 10.25, 9.85, 9, 8, 7, 6, 5.75, 5.25, 5, 4.75, 4,3.95, 3.25, 3.05, 3, 2.85, 2.75,2.25, 2, 1.95, 1.85, 1.75, 1.65, 1.5, 1.45, 1.25, 1.05, 1.01,1.0,1.0, 1.0,1,1,0.85, 0.85,0.8,0.8,0.75, 0.75,0.65,0.6,0.5,0.5,0.5,0.5,0.25]

thirty_microfarad_charging = [15, 10, 9.5, 9.0, 8.75, 8.25, 7.75, 7.25, 7, 6.75, 6, 5.75, 5.5,5.1, 5, 4.75, 4.5, 4.05, 4, 3.85, 3.5, 3.25, 3, 3, 2.95, 2.85, 2.65]
print(len(thirty_microfarad_charging))
def linearize(L: list):
    new_list = np.array(L)
    Linearized_list = np.log(new_list)
    return Linearized_list



