#This is a simple Kramer's rule Calculator. It can do 2 by 2 and 3 by 3 Linear Systems of equations
import numpy as np
def two_by_two(x1,x2,y1,y2,c1,c2):
    full_matrix = np.array([[x1, y1], 
                            [x2,y2]])
    full_matrix_determinant = np.linalg.det(full_matrix)
    x_determinant_matrix = np.array([[c1, y1], 
                                     [c2,y2]])
    x_determinant = np.linalg.det(x_determinant_matrix)
    x = x_determinant / full_matrix_determinant
    y_determinant_matrix = np.array([[x1, c1], 
                                     [x2,c2]])
    y_determinant = np.linalg.det(y_determinant_matrix)
    y = y_determinant / full_matrix_determinant

    return x,y

print(two_by_two(2,4,8,6,9,1))