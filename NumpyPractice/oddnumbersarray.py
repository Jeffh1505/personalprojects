import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_arr = arr % 2 == 1
print(arr)

print(arr[odd_arr])

arr[odd_arr] = -1

print(arr)