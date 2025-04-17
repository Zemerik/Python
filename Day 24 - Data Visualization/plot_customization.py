import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Customized line plot
x = [1, 2, 3, 4]
y = [10, 30, 25, 40]

plt.plot(x, y, 
         color='#2ecc71', 
         linestyle='--',
         marker='o',
         linewidth=2,
         markersize=8,
         label='Growth')

plt.title("Customized Plot", fontsize=14)
plt.xlabel("Quarter", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()