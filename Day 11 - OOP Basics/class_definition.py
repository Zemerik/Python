# Basic class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}!")

# Create instance
person1 = Person("Joe", 30)
print(person1.name)
person1.greet()