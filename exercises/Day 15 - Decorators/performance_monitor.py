"""
Exercise 1: Performance Monitor Decorator
Create a decorator that:
- Measures function execution time
- Validates input arguments (e.g., positive numbers)
- Logs function calls to a file
"""

import time
import functools
import logging
from datetime import datetime
import os

class PerformanceMonitor:
    """Performance monitoring decorator with validation and logging"""
    
    def __init__(self, log_file="function_calls.log"):
        """Initialize the performance monitor"""
        self.log_file = log_file
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def __call__(self, func):
        """Main decorator method"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function info
            func_name = func.__name__
            start_time = time.time()
            
            # Log function call
            logging.info(f"Function '{func_name}' called with args: {args}, kwargs: {kwargs}")
            
            try:
                # Validate arguments
                self.validate_arguments(func_name, args, kwargs)
                
                # Execute function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Log successful execution
                logging.info(f"Function '{func_name}' completed successfully in {execution_time:.4f} seconds")
                
                return result
                
            except Exception as e:
                # Calculate execution time even for failed calls
                execution_time = time.time() - start_time
                
                # Log error
                logging.error(f"Function '{func_name}' failed after {execution_time:.4f} seconds: {str(e)}")
                raise
        
        return wrapper
    
    def validate_arguments(self, func_name, args, kwargs):
        """Validate function arguments based on function name"""
        if func_name in ['calculate_factorial', 'fibonacci']:
            # Validate that first argument is a positive integer
            if args and len(args) > 0:
                if not isinstance(args[0], int) or args[0] < 0:
                    raise ValueError(f"Function '{func_name}' requires a non-negative integer, got {args[0]}")
        
        elif func_name in ['calculate_area', 'calculate_volume']:
            # Validate that all numeric arguments are positive
            for i, arg in enumerate(args):
                if isinstance(arg, (int, float)) and arg <= 0:
                    raise ValueError(f"Function '{func_name}' requires positive numbers, got {arg} at position {i}")
        
        elif func_name in ['divide_numbers']:
            # Validate that divisor is not zero
            if len(args) >= 2 and args[1] == 0:
                raise ValueError("Division by zero is not allowed")

def performance_monitor(log_file="function_calls.log"):
    """Alternative decorator function approach"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Setup logging for this call
            logging.basicConfig(
                filename=log_file,
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            func_name = func.__name__
            start_time = time.time()
            
            # Log function call
            logging.info(f"Function '{func_name}' called with args: {args}, kwargs: {kwargs}")
            
            try:
                # Execute function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Log successful execution
                logging.info(f"Function '{func_name}' completed successfully in {execution_time:.4f} seconds")
                
                return result
                
            except Exception as e:
                # Calculate execution time even for failed calls
                execution_time = time.time() - start_time
                
                # Log error
                logging.error(f"Function '{func_name}' failed after {execution_time:.4f} seconds: {str(e)}")
                raise
        
        return wrapper
    return decorator

# Example functions to demonstrate the decorator
@PerformanceMonitor("math_operations.log")
def calculate_factorial(n):
    """Calculate factorial of a number"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
        time.sleep(0.01)  # Simulate some processing time
    return result

@PerformanceMonitor("math_operations.log")
def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        time.sleep(0.005)  # Simulate some processing time
    return b

@PerformanceMonitor("geometry_operations.log")
def calculate_area(length, width):
    """Calculate area of a rectangle"""
    time.sleep(0.02)  # Simulate processing time
    return length * width

@PerformanceMonitor("geometry_operations.log")
def calculate_volume(length, width, height):
    """Calculate volume of a rectangular prism"""
    time.sleep(0.03)  # Simulate processing time
    return length * width * height

@performance_monitor("division_operations.log")
def divide_numbers(a, b):
    """Divide two numbers"""
    time.sleep(0.01)  # Simulate processing time
    return a / b

class MathOperations:
    """Class with decorated methods"""
    
    def __init__(self):
        self.monitor = PerformanceMonitor("class_operations.log")
    
    @property
    def decorated_method(self):
        """Property to get decorated method"""
        return self.monitor(self._method)
    
    def _method(self, x):
        """Internal method to be decorated"""
        time.sleep(0.01)
        return x * 2

def demonstrate_decorator():
    """Demonstrate the performance monitor decorator"""
    print("=== Performance Monitor Decorator Demonstration ===")
    
    # Test factorial calculation
    print("\n1. Testing factorial calculation:")
    try:
        result = calculate_factorial(5)
        print(f"   Factorial of 5: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test with invalid input
    print("\n2. Testing with invalid input:")
    try:
        result = calculate_factorial(-1)
        print(f"   Factorial of -1: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test Fibonacci
    print("\n3. Testing Fibonacci:")
    try:
        result = fibonacci(10)
        print(f"   10th Fibonacci number: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test area calculation
    print("\n4. Testing area calculation:")
    try:
        result = calculate_area(5, 3)
        print(f"   Area of 5x3 rectangle: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test with negative dimensions
    print("\n5. Testing with negative dimensions:")
    try:
        result = calculate_area(-5, 3)
        print(f"   Area of -5x3 rectangle: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test volume calculation
    print("\n6. Testing volume calculation:")
    try:
        result = calculate_volume(2, 3, 4)
        print(f"   Volume of 2x3x4 prism: {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test division
    print("\n7. Testing division:")
    try:
        result = divide_numbers(10, 2)
        print(f"   10 / 2 = {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test division by zero
    print("\n8. Testing division by zero:")
    try:
        result = divide_numbers(10, 0)
        print(f"   10 / 0 = {result}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test class method
    print("\n9. Testing class method:")
    math_ops = MathOperations()
    try:
        result = math_ops.decorated_method(7)
        print(f"   7 * 2 = {result}")
    except Exception as e:
        print(f"   Error: {e}")

def show_log_files():
    """Show the contents of log files"""
    print("\n=== Log Files Contents ===")
    
    log_files = [
        "math_operations.log",
        "geometry_operations.log", 
        "division_operations.log",
        "class_operations.log"
    ]
    
    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"\n{log_file}:")
            try:
                with open(log_file, 'r') as f:
                    content = f.read()
                    if content.strip():
                        print(content)
                    else:
                        print("   (Empty file)")
            except Exception as e:
                print(f"   Error reading file: {e}")
        else:
            print(f"\n{log_file}: (File not found)")

def main():
    """Main function to demonstrate the performance monitor"""
    print("=== Performance Monitor Decorator ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Run decorator demonstration")
        print("2. Show log files")
        print("3. Clear log files")
        print("4. Exit")
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                demonstrate_decorator()
            
            elif choice == '2':
                show_log_files()
            
            elif choice == '3':
                log_files = [
                    "math_operations.log",
                    "geometry_operations.log", 
                    "division_operations.log",
                    "class_operations.log"
                ]
                for log_file in log_files:
                    if os.path.exists(log_file):
                        os.remove(log_file)
                        print(f"Removed {log_file}")
                print("All log files cleared.")
            
            elif choice == '4':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 4.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 