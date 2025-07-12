"""
Exercise 1: Math Utils Module
Create a math_utils.py module with:
- Function to calculate circle area (πr²)
- Function to generate Fibonacci sequence
- Test code using if __name__ == "__main__"
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle using the formula πr²
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def generate_fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms
    
    Args:
        n (int): Number of terms to generate
        
    Returns:
        list: List containing the Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

def calculate_factorial(n):
    """
    Calculate factorial of a number
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test code that runs only when the module is executed directly
if __name__ == "__main__":
    print("=== Math Utils Module Test ===")
    
    # Test circle area calculation
    print("\n1. Testing Circle Area Calculation:")
    test_radii = [1, 2.5, 5, 10]
    for radius in test_radii:
        area = calculate_circle_area(radius)
        print(f"   Radius: {radius}, Area: {area:.2f}")
    
    # Test Fibonacci sequence generation
    print("\n2. Testing Fibonacci Sequence Generation:")
    test_terms = [5, 8, 10]
    for terms in test_terms:
        sequence = generate_fibonacci_sequence(terms)
        print(f"   First {terms} terms: {sequence}")
    
    # Test factorial calculation
    print("\n3. Testing Factorial Calculation:")
    test_factorials = [0, 1, 5, 7]
    for num in test_factorials:
        factorial = calculate_factorial(num)
        print(f"   {num}! = {factorial}")
    
    # Test prime number checking
    print("\n4. Testing Prime Number Check:")
    test_numbers = [2, 3, 4, 17, 25, 29]
    for num in test_numbers:
        is_prime_num = is_prime(num)
        print(f"   {num} is {'prime' if is_prime_num else 'not prime'}")
    
    print("\n=== All tests completed! ===") 