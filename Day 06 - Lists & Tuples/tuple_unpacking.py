# Basic tuple
dimensions = (1920, 1080)
width, height = dimensions
print(f"Resolution: {width}x{height}")

# Multiple return values
def get_user_info():
    return "John", "Doe", 30

first, last, age = get_user_info()
print(f"{first} {last}, {age} years old")

# Extended unpacking
values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(f"First: {a}, Second: {b}, Rest: {rest}")