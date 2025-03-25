from functools import reduce

# Sum numbers
numbers = [1, 2, 3, 4]
sum_total = reduce(lambda a, b: a + b, numbers)
print(f"Sum: {sum_total}")

# Find maximum
max_num = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Maximum: {max_num}")