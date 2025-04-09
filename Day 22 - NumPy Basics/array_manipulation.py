import numpy as np

# Reshaping
arr = np.arange(12)
print("Original shape:", arr.shape)
matrix = arr.reshape(3,4)
print("Reshaped:\n", matrix)

# Stacking
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Vertical stack:\n", np.vstack((a,b)))
print("Horizontal stack:", np.hstack((a,b)))

# Advanced indexing
data = np.random.randint(0,50,(5,5))
print("First column:", data[:,0])
print("Diagonal:", data.diagonal())