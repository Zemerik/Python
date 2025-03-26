# Dictionary comprehension
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Lengths: {name_lengths}")

# Set comprehension
words = ["hello", "world", "hello", "python"]
unique_lengths = {len(word) for word in words}
print(f"Unique lengths: {unique_lengths}")

# File processing
with open("data.txt") as f:
    lines = [line.strip().upper() for line in f]
print(f"Processed lines: {lines}")