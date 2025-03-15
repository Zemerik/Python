# Positional arguments
def format_name(first, last):
    """Formats a full name from first and last name"""
    return f"{first.title()} {last.title()}"

# Default parameters
def calculate_area(length, width=1):
    """Calculates area (defaults to square if width omitted)"""
    return length * width

# Keyword arguments
print(format_name(first="john", last="doe"))
print(calculate_area(width=4, length=5))  # Order doesn't matter

# Variable-length arguments (*args)
def average(*numbers):
    """Calculates average of any number of values"""
    return sum(numbers) / len(numbers) if numbers else 0

print(f"Average: {average(4, 7, 9, 2):.2f}")