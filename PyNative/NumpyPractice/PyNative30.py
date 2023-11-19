import numpy as np

array_to_split = np.array(range(10,34)).reshape(8,3)

print("Original array:",array_to_split)

splitted_array = np.split(array_to_split, 4)

print(splitted_array)