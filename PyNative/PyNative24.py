import numpy as np
arr = np.array([[64392, 31655], [32579, 0], [49248, 462], [0,0]])

print(arr)
dimensions = 0
for dimension in arr.shape:
    dimensions += 1
print(f"Array shape:{arr.shape} \nArray dimensions: {dimensions} ")