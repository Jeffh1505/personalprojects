import numpy as np
arr = np.array([64392, 32579, 49248, 0, 31655, 0, 462, 0])

print(arr)
dimensions = 0
for dimension in arr.shape:
    dimensions += 1
print(f"Array shape:{arr.shape} \nArray dimensions: {dimensions} ")