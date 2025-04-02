# List comprehension (eager)
squares_list = [x**2 for x in range(1000000)]  # Stores all values

# Generator expression (lazy)
squares_gen = (x**2 for x in range(1000000))  # Generates on demand

print("Memory used (list):", squares_list.__sizeof__())
print("Memory used (gen):", squares_gen.__sizeof__())