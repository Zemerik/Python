# Handling specific exceptions
try:
    file = open("missing.txt", "r")
    value = int("abc")
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid conversion to integer")