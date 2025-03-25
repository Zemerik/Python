# Filter even numbers
numbers = range(1, 11)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter valid emails
emails = ["user@test.com", "invalid", "admin@domain.org"]
valid_emails = list(filter(lambda e: '@' in e and '.' in e.split('@')[1], emails))
print(f"Valid emails: {valid_emails}")