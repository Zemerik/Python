# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Unrealistic age")
        
try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")

# Custom exception
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Missing @ symbol")