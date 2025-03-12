import numpy as np

arr = np.array([5, 3, 9, 3, 7, 9, 2, 9])

nines = np.where(arr == 9)
print(nines)
arr[arr==3] = 0
print(arr)
sorted_arr = np.sort(arr)
print(sorted_arr)