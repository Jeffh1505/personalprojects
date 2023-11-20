import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]]).reshape(3,1)


print(sampleArray)

sampleArray = sampleArray[:,:2]
print(sampleArray)

new_array = np.hstack((sampleArray, newColumn))

print(new_array)