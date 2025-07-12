# Basic error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Generic exception
try:
    print(undefined_variable)
except Exception as e:
    print(f"Error occurred: {str(e)}")