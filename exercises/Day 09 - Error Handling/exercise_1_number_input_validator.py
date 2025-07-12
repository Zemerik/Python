"""
Exercise 1: Number Input Validator
Create a number input validator that:
- Keeps asking for input until valid number
- Handles both ValueError and KeyboardInterrupt
- Prints "Thank you!" on successful input
"""

class NumberInputValidator:
    def __init__(self):
        """Initialize the number input validator"""
        self.attempts = 0
        self.max_attempts = 10
    
    def get_valid_number(self, prompt="Enter a number: ", min_value=None, max_value=None):
        """
        Get a valid number from user input
        
        Args:
            prompt (str): The prompt to display to the user
            min_value (float, optional): Minimum allowed value
            max_value (float, optional): Maximum allowed value
        
        Returns:
            float: The valid number entered by the user
        """
        while True:
            try:
                self.attempts += 1
                if self.attempts > self.max_attempts:
                    print(f"Too many attempts ({self.max_attempts}). Exiting...")
                    return None
                
                user_input = input(prompt)
                number = float(user_input)
                
                # Validate range if specified
                if min_value is not None and number < min_value:
                    print(f"Number must be at least {min_value}")
                    continue
                
                if max_value is not None and number > max_value:
                    print(f"Number must be at most {max_value}")
                    continue
                
                print("Thank you!")
                return number
                
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                if self.attempts >= 3:
                    print("Hint: Try entering a number like 42 or 3.14")
                
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                print("Thank you for trying!")
                return None
    
    def get_integer(self, prompt="Enter an integer: ", min_value=None, max_value=None):
        """
        Get a valid integer from user input
        
        Args:
            prompt (str): The prompt to display to the user
            min_value (int, optional): Minimum allowed value
            max_value (int, optional): Maximum allowed value
        
        Returns:
            int: The valid integer entered by the user
        """
        while True:
            try:
                self.attempts += 1
                if self.attempts > self.max_attempts:
                    print(f"Too many attempts ({self.max_attempts}). Exiting...")
                    return None
                
                user_input = input(prompt)
                number = int(user_input)
                
                # Validate range if specified
                if min_value is not None and number < min_value:
                    print(f"Number must be at least {min_value}")
                    continue
                
                if max_value is not None and number > max_value:
                    print(f"Number must be at most {max_value}")
                    continue
                
                print("Thank you!")
                return number
                
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                if self.attempts >= 3:
                    print("Hint: Try entering a whole number like 42")
                
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                print("Thank you for trying!")
                return None
    
    def reset_attempts(self):
        """Reset the attempt counter"""
        self.attempts = 0
    
    def get_attempts(self):
        """Get the number of attempts made"""
        return self.attempts

def demonstrate_validator():
    """Demonstrate the number input validator"""
    print("=== Number Input Validator Demo ===")
    validator = NumberInputValidator()
    
    # Demo 1: Basic number input
    print("\n1. Basic number input:")
    number = validator.get_valid_number("Enter any number: ")
    if number is not None:
        print(f"You entered: {number}")
    
    validator.reset_attempts()
    
    # Demo 2: Integer input with range
    print("\n2. Integer input with range (1-100):")
    integer = validator.get_integer("Enter an integer between 1 and 100: ", 1, 100)
    if integer is not None:
        print(f"You entered: {integer}")
    
    validator.reset_attempts()
    
    # Demo 3: Float input with minimum value
    print("\n3. Float input with minimum value (0.0):")
    positive_number = validator.get_valid_number("Enter a positive number: ", 0.0)
    if positive_number is not None:
        print(f"You entered: {positive_number}")
    
    print(f"\nTotal attempts across all demos: {validator.get_attempts()}")

def main():
    """Main function to run the number input validator"""
    print("=== Number Input Validator ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Enter any number")
        print("2. Enter integer (1-100)")
        print("3. Enter positive number")
        print("4. Run demo")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                validator = NumberInputValidator()
                number = validator.get_valid_number()
                if number is not None:
                    print(f"Result: {number}")
            
            elif choice == '2':
                validator = NumberInputValidator()
                integer = validator.get_integer("Enter integer (1-100): ", 1, 100)
                if integer is not None:
                    print(f"Result: {integer}")
            
            elif choice == '3':
                validator = NumberInputValidator()
                positive = validator.get_valid_number("Enter positive number: ", 0.0)
                if positive is not None:
                    print(f"Result: {positive}")
            
            elif choice == '4':
                demonstrate_validator()
            
            elif choice == '5':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 