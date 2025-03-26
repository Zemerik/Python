# Matrix flattening
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# Multiplication table
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication Table:")
for row in table:
    print(row)