import re

# Simple match
text = "The quick brown fox"
match = re.search(r"brown", text)
print("Found brown:", bool(match))

# Character set
vowels = re.findall(r"[aeiou]", text, re.I)
print("Vowels:", vowels)

# Quantifiers
numbers = "123 4567 89012"
print("3-4 digits:", re.findall(r"\d{3,4}", numbers))