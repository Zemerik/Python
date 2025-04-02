def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Usage
for num in countdown(5):
    print(f"T-minus {num}")

# Output: 5, 4, 3, 2, 1