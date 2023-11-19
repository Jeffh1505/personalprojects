import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print(sampleArray)

sorted_array1 = sampleArray[:,sampleArray[1,:].argsort()]
print(sorted_array1)

sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)