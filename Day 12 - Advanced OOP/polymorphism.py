class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic function
def animal_sound(animal):
    print(animal.speak())

# Usage
animals = [Dog(), Cat()]
for a in animals:
    animal_sound(a)