import numpy as np

array_to_split = np.array(range(10,34)).reshape(8,3)

print(array_to_split)

array1 = array_to_split[:2,:]
print(array1)