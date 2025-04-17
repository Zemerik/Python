import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10,8))

# Plot 1
x = np.arange(0, 10, 0.1)
axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("Sine Wave")

# Plot 2
axs[0,1].scatter(np.random.rand(50), np.random.rand(50), c='orange')

# Plot 3
categories = ['A', 'B', 'C']
values = [25, 40, 30]
axs[1,0].bar(categories, values, color='green')

# Plot 4
axs[1,1].pie([30, 20, 50], labels=['X', 'Y', 'Z'])

plt.tight_layout()
plt.show()