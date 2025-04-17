import matplotlib.pyplot as plt
import numpy as np

# Histogram
data = np.random.normal(170, 10, 250)
plt.hist(data, bins=20, edgecolor='black')
plt.title("Height Distribution")
plt.show()

# Boxplot
data = [np.random.normal(0, std, 100) for std in range(1,4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.xticks([1,2,3], ['A', 'B', 'C'])
plt.show()

# Heatmap
data = np.random.rand(10,10)
plt.imshow(data, cmap='viridis')
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()