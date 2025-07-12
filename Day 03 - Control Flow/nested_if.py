# Nested if-else example
age = 25
has_membership = True

if age >= 18:
    print("Adult verified")
    if has_membership:
        print("Welcome premium member!")
    else:
        print("Regular adult access")
else:
    print("Minor access only")

# Temperature and humidity check
temperature = 28
humidity = 85

if temperature > 25:
    print("High temperature warning")
    if humidity > 80:
        print("Heat advisory: High temp + humidity!")
    else:
        print("Stay hydrated")
else:
    print("Normal temperature range")