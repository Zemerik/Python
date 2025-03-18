# Dictionary creation
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "CS"]
}

# Accessing values
print(student["name"])
print(student.get("grade", "N/A"))  # Safe access

# Modifying dict
student["email"] = "alice@school.edu"
del student["age"]

# Dictionary methods
print("Keys:", student.keys())
print("Items:", student.items())