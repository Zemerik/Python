"""
Exercise 2: Temperature Conversion Package
Build a temperature conversion package:
- Create temperature.py with C/F/K conversions
- Import it in weather_report.py
- Handle different measurement systems
"""

# This is the temperature.py module
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature between different units
    
    Args:
        value (float): Temperature value
        from_unit (str): Source unit ('C', 'F', 'K')
        to_unit (str): Target unit ('C', 'F', 'K')
    
    Returns:
        float: Converted temperature value
    """
    # Convert to Celsius first
    if from_unit.upper() == 'C':
        celsius = value
    elif from_unit.upper() == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit.upper() == 'K':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unsupported unit: {from_unit}")
    
    # Convert from Celsius to target unit
    if to_unit.upper() == 'C':
        return celsius
    elif to_unit.upper() == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_unit.upper() == 'K':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unsupported unit: {to_unit}")

def get_temperature_description(celsius):
    """
    Get a description of the temperature in Celsius
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        str: Description of the temperature
    """
    if celsius < -10:
        return "Very Cold"
    elif celsius < 0:
        return "Cold"
    elif celsius < 10:
        return "Cool"
    elif celsius < 20:
        return "Mild"
    elif celsius < 30:
        return "Warm"
    elif celsius < 40:
        return "Hot"
    else:
        return "Very Hot"

# Test the module when run directly
if __name__ == "__main__":
    print("=== Temperature Conversion Module Test ===")
    
    # Test basic conversions
    print("\nBasic Conversions:")
    print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
    print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
    print(f"25°C = {celsius_to_kelvin(25):.1f}K")
    print(f"298.15K = {kelvin_to_celsius(298.15):.1f}°C")
    
    # Test the general conversion function
    print("\nGeneral Conversion Function:")
    print(f"25°C to °F: {convert_temperature(25, 'C', 'F'):.1f}°F")
    print(f"77°F to K: {convert_temperature(77, 'F', 'K'):.1f}K")
    print(f"298.15K to °F: {convert_temperature(298.15, 'K', 'F'):.1f}°F")
    
    # Test temperature descriptions
    print("\nTemperature Descriptions:")
    test_temps = [-15, 0, 15, 25, 35, 45]
    for temp in test_temps:
        desc = get_temperature_description(temp)
        print(f"{temp}°C: {desc}")
    
    print("\n=== Module test completed! ===") 