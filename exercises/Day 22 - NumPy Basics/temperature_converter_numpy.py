"""
Exercise 1: NumPy Temperature Converter
Create a temperature converter that:
- Converts 2D Celsius array to Fahrenheit
- Filters values below freezing (<0°C)
- Calculates daily temperature ranges
"""

import numpy as np

class TemperatureConverterNumPy:
    """Temperature converter using NumPy arrays"""
    
    def __init__(self, days=5, hours=4):
        self.days = days
        self.hours = hours
        self.celsius = np.random.uniform(-10, 35, size=(days, hours))
    
    def convert_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit
    
    def filter_below_freezing(self):
        below_freezing = self.celsius < 0
        return self.celsius[below_freezing]
    
    def daily_ranges(self):
        return np.ptp(self.celsius, axis=1)  # Peak-to-peak (max-min) per day
    
    def display(self):
        print("Celsius temperatures:")
        print(self.celsius)
        print("\nFahrenheit temperatures:")
        print(self.convert_to_fahrenheit())
        print("\nValues below freezing:")
        print(self.filter_below_freezing())
        print("\nDaily temperature ranges:")
        print(self.daily_ranges())

def main():
    print("=== NumPy Temperature Converter ===")
    converter = TemperatureConverterNumPy()
    converter.display()

if __name__ == "__main__":
    main() 