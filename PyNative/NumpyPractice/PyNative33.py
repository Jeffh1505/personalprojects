import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]])


print(sampleArray.shape)
print(newColumn.shape)
sampleArray = sampleArray[:,:2]
print(sampleArray)

new_array = np.hstack((sampleArray, newColumn))