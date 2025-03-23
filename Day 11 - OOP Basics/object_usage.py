from class_definition import Person

# Multiple instances
student = Person("Harry", 20)
teacher = Person("Dr. Van", 45)

print(f"{student.name} is {student.age} years old")
teacher.greet()

# Modify attributes
student.age = 21
print(f"Updated age: {student.age}")