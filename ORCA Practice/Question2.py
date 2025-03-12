import numpy as np

arr = np.array([[3, 7, np.nan, 12], 
                [15, np.nan, 6, 2], 
                [np.nan, 4, 8, 10]])
arr[arr==7] = 14
print(arr)
nan_indicies = np.where(arr == np.nan)
print(nan_indicies)
max_cols = np.nanmax(arr, axis=0)
print(max_cols)
descending_sort = np.sort(arr)[::-1]
print(descending_sort)