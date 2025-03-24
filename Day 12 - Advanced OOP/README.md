# Day 12: Advanced Object-Oriented Programming

## What You'll Learn:
- Class inheritance hierarchies
- Method overriding and polymorphism
- Abstract base classes (ABC)
- Multiple inheritance and MRO

## Files:
1. `inheritance.py` - Multi-level inheritance
2. `polymorphism.py` - Runtime polymorphism
3. `abstract_classes.py` - Using ABC module
4. `multiple_inheritance.py` - Diamond problem resolution

## Exercises:
1. Create a `Shape` class hierarchy with:
   - Abstract `area()` and `perimeter()` methods
   - Concrete `Circle`, `Rectangle`, and `Triangle` subclasses
   - Polymorphic method calls

2. Build a payment processor system with:
   - Base `PaymentMethod` class
   - `CreditCard`, `PayPal`, and `Crypto` subclasses
   - Common `process_payment()` interface