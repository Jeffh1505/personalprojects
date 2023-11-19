#Load Library
import numpy as np
import SciPy
#Create a Matrix
matrix = np.array([[0,0],[0,1],[3,0]])
print(matrix)
#Create Compressed Sparse Row(CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)