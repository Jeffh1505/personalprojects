import numpy as np

sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print(sampleArray[sampleArray % 2 == 1, sampleArray % 2 ==0])


