"""
Exercise 1: Temperature Conversion Program
Create a temperature conversion program that:
- Has separate functions for Celsius to Fahrenheit and Fahrenheit to Celsius
- Takes user input for temperature and conversion type
- Returns formatted conversion result
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9


def get_temperature_input():
    """Get temperature value from user"""
    while True:
        try:
            temp = float(input("Enter temperature: "))
            return temp
        except ValueError:
            print("Please enter a valid number.")


def get_conversion_type():
    """Get conversion type from user"""
    print("\nConversion options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    while True:
        try:
            choice = int(input("Select conversion type (1 or 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Please select 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")


def format_result(original_temp, converted_temp, from_unit, to_unit):
    """Format and return the conversion result"""
    return f"{original_temp}°{from_unit} = {converted_temp:.1f}°{to_unit}"


def perform_conversion():
    """Main conversion logic"""
    # Get user input
    temperature = get_temperature_input()
    conversion_type = get_conversion_type()
    
    # Perform conversion
    if conversion_type == 1:
        # Celsius to Fahrenheit
        converted = celsius_to_fahrenheit(temperature)
        result = format_result(temperature, converted, "C", "F")
    else:
        # Fahrenheit to Celsius
        converted = fahrenheit_to_celsius(temperature)
        result = format_result(temperature, converted, "F", "C")
    
    return result


def main():
    print("=== Temperature Converter ===")
    
    while True:
        # Perform conversion
        result = perform_conversion()
        print(f"\nResult: {result}")
        
        # Ask if user wants to convert another temperature
        another = input("\nConvert another temperature? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break
        print("\n" + "="*30 + "\n")

if __name__ == "__main__":
    main() 