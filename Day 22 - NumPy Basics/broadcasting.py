import numpy as np

# Broadcasting example
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,20,30])

# Operations between different shapes
print("Matrix + vector:\n", matrix + vector)

# Conditional operations
temps = np.random.randint(-10,40,(5,5))
print("Freezing mask:\n", temps < 0)

# Matrix operations
identity = np.eye(3)
matrix = np.arange(9).reshape(3,3)
print("Matrix multiplication:\n", identity @ matrix)