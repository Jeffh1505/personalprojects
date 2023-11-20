import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print("Sample array: ",sampleArray)

max_in_axis0 = np.max(sampleArray, 0)

min_in_axis1 = np.min(sampleArray, 1)

print("Max in axis 0:",max_in_axis0)

print("Min in axis 1: ", min_in_axis1)