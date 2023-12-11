import numpy as np

square = np.array([[4, 3, 7], 
                   [8, 1, 2], 
                   [2, 0, 9]])

def compare_diagonal_sums(square):
    diagonal1_sum = square[0,0] + square[1,1] + square[2,2]
    diagonal2_sum = square[0,2] + square[1,1] + square[2,0]
    if diagonal1_sum == diagonal2_sum:
        return True
    else:
        return False
    
print(compare_diagonal_sums(square))