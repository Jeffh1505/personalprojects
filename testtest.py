import numpy as np

square = np.array([[4, 3, 7], 
                   [8, 1, 2], 
                   [2, 0, 9]])

def compare_diagonal_sums(square):
    diagonal1_sum = 0
    diagonal2_sum = 0
    for i in range(0, len(square)):
        length = len(square)-1
        diagonal1_sum += square[i,i]
        diagonal2_sum += square[length-i, length-i]
        print("diagonal1:",diagonal1_sum)
        print("diagonal2:",diagonal2_sum)
    if diagonal1_sum == diagonal2_sum:
        return True
    else:
        return False
    
print(compare_diagonal_sums(square))