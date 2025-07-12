"""
Weather Report Application
This script imports the temperature module and uses it to create weather reports
"""

# Import the temperature module
# Note: In a real project, you would have temperature.py in the same directory
# For this exercise, we'll simulate the import by including the functions directly

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def get_temperature_description(celsius):
    """Get a description of the temperature in Celsius"""
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

def create_weather_report(location, temp_celsius, humidity, conditions):
    """
    Create a comprehensive weather report
    
    Args:
        location (str): Location name
        temp_celsius (float): Temperature in Celsius
        humidity (int): Humidity percentage
        conditions (str): Weather conditions
    
    Returns:
        dict: Weather report data
    """
    # Convert temperatures to different units
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
    temp_kelvin = celsius_to_kelvin(temp_celsius)
    
    # Get temperature description
    temp_description = get_temperature_description(temp_celsius)
    
    # Create the report
    report = {
        'location': location,
        'temperature': {
            'celsius': temp_celsius,
            'fahrenheit': temp_fahrenheit,
            'kelvin': temp_kelvin
        },
        'description': temp_description,
        'humidity': humidity,
        'conditions': conditions,
        'timestamp': '2024-01-15 14:30:00'  # Simulated timestamp
    }
    
    return report

def display_weather_report(report):
    """Display the weather report in a formatted way"""
    print(f"\n=== Weather Report for {report['location']} ===")
    print(f"Temperature: {report['temperature']['celsius']}°C / {report['temperature']['fahrenheit']}°F / {report['temperature']['kelvin']}K")
    print(f"Description: {report['description']}")
    print(f"Humidity: {report['humidity']}%")
    print(f"Conditions: {report['conditions']}")
    print(f"Report Time: {report['timestamp']}")

def get_weather_data():
    """Get weather data from user input"""
    location = input("Enter location: ")
    
    while True:
        try:
            temp = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            humidity = int(input("Enter humidity percentage (0-100): "))
            if 0 <= humidity <= 100:
                break
            else:
                print("Humidity must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    conditions = input("Enter weather conditions (e.g., Sunny, Rainy, Cloudy): ")
    
    return location, temp, humidity, conditions

def main():
    print("=== Weather Report Generator ===")
    print("This application uses the temperature module to create weather reports.")
    
    while True:
        # Get weather data
        location, temp, humidity, conditions = get_weather_data()
        
        # Create and display report
        report = create_weather_report(location, temp, humidity, conditions)
        display_weather_report(report)
        
        # Ask if user wants to create another report
        another = input("\nCreate another weather report? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 