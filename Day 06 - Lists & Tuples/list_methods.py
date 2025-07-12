# List creation and basic methods
fruits = ["apple", "banana"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("orange")
fruits.insert(1, "mango")
print(f"After additions: {fruits}")

# Removing elements
fruits.remove("banana")
popped = fruits.pop()
print(f"After removals: {fruits}, Popped: {popped}")

# Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(f"Sorted numbers: {numbers}")