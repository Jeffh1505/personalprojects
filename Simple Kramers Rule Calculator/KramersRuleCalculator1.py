#This is a simple Kramer's rule Calculator. It can do 2 by 2 and 3 by 3 Linear Systems of equations
import numpy as np
def two_by_two(x1,x2,y1,y2,c1,c2):
    #This function calculates a two by two linear system of equations, x1 and x2 are the coefficients on the x variable, 
    #y1 and y2 are the coefficients of the y variable and c1 and c2 are the constants
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

    return f"x = {x}\n y = {y}"

def three_by_three(x1,x2,x3,y1,y2,y3,z1,z2,z3,c1,c2,c3):
    #This function calculates a three by three system of equations
    full_matrix = np.array([[x1, y1, z1],
                            [x2, y2, z2],
                            [x3, y3, z3]])
    full_matrix_determinant = np.linalg.det(full_matrix)
    x_determinant_matrix = np.array([[c1, y1, z1], 
                                     [c2,y2, z2],
                                     [c3, y3,z3]])
    x_determinant = np.linalg.det(x_determinant_matrix)
    x = x_determinant / full_matrix_determinant 
    y_determinant_matrix = np.array([[x1, c1, z1], 
                                     [x2,c2, z2],
                                     [x3, c3,z3]])
    y_determinant = np.linalg.det(y_determinant_matrix)
    y = y_determinant / full_matrix_determinant
    z_determinant_matrix = np.array([[x1, y1, c1], 
                                     [x2,y2, c2],
                                     [x3, y3,c3]])
    z_determinant = np.linalg.det(z_determinant_matrix)
    z = z_determinant / full_matrix_determinant
    return f"x = {x}\n y = {y} \n z = {z}"

print(three_by_three(2,5,1,7,3,6,9,8,4,5,2,4))
    

