import numpy as np
from numpy import linalg

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

B = np.array([
    [3, 1, 4],
    [2, 6, 1], 
    [2, 9, 7]])

# a. A + B
print(np.add(A, B))
print('\n')

# b. A X B
print(np.multiply(A, B))
print('\n')

# c. Determinate of A
print(linalg.det(A))
print('\n')

# d. Inverse of B
print(linalg.inv(B))
print('\n')

# e. Eigenvalues of A
print(linalg.eigvals(A))
print('\n')