import numpy as np

array_to_split = np.array(range(10,34)).reshape(8,3)

print("Original array:",array_to_split)

array1 = array_to_split[:2,:]
print("Array 1: ",array1)

array2 = array_to_split[2:4,:]
print("Array 2: ", array2)