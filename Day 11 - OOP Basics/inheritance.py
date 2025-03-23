# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal sound!")

# Child class
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Usage
generic = Animal("Unknown")
generic.speak()

buddy = Dog("Buddy")
buddy.speak()  # Overrides parent method