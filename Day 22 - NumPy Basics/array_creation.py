import numpy as np

# Different creation methods
arr1 = np.array([1, 2, 3])          # From list
arr2 = np.arange(0, 10, 2)          # Range array
arr3 = np.zeros((2,3))               # Zero matrix
arr4 = np.random.rand(3,3)          # Random values

print("1D Array:", arr1)
print("2D Zeros:\n", arr3)
print("Random Matrix:\n", arr4)