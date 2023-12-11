import numpy as np

square = np.array([[4, 3, 7], 
                   [8, 1, 2], 
                   [2, 0, 9]])

def compare_diagonal_sums(square):
    diagonal1_sum = 0
    diagonal2_sum = 0
    size = len(square)  # Size of the square matrix
    print(size)
    for i in range(size):
        diagonal1_sum += square[i, i]  # Sum of main diagonal
        diagonal2_sum += square[i, size - i - 1]
        print("diagonal1: ",diagonal1_sum)
        print("diagonal2: ",diagonal2_sum)  # Sum of secondary diagonal
    
    return diagonal1_sum == diagonal2_sum

print(compare_diagonal_sums(square))
