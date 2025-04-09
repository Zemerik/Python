import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print("Addition:", a + b)
print("Multiplication:", a * 2)
print("Dot product:", np.dot(a, b))

# Statistical operations
matrix = np.random.randint(0,100,(5,5))
print("Matrix:\n", matrix)
print("Column means:", matrix.mean(axis=0))
print("Overall max:", matrix.max())