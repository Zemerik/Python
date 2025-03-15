# Simple return
def square(number):
    return number ** 2

# Returning multiple values
def split_name(full_name):
    names = full_name.split()
    return names[0], names[-1]  # Returns tuple

# Using returned values
result = square(4)
print(f"Square of 4: {result}")

first, last = split_name("Marie Curie")
print(f"First: {first}, Last: {last}")

# Returning complex data
def analyze_number(n):
    is_even = n % 2 == 0
    absolute = abs(n)
    return {
        "original": n,
        "even": is_even,
        "absolute": absolute
    }

print(analyze_number(-5))