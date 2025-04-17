import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("Sine Wave")
plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [25, 40, 30]
plt.bar(categories, values)
plt.ylabel("Counts")
plt.show()

# Scatter plot
x = np.random.randn(100)
y = x + np.random.randn(100)*0.5
plt.scatter(x, y, alpha=0.6)
plt.xlabel("X Values")
plt.show()