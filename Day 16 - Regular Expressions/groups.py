import re

# Capturing groups
date = "2023-12-25"
match = re.match(r"(\d{4})-(\d{2})-(\d{2})", date)
print(f"Year: {match.group(1)}, Month: {match.group(2)}")

# Named groups
text = "James: 42"
match = re.search(r"(?P<name>\w+): (?P<age>\d+)", text)
print(f"{match.group('name')} is {match.group('age')}")

# Non-capturing group
print("Plurals:", re.findall(r"\b\w+(?:s|es)\b", "boxes cats dog"))