"""
Exercise 1: Temperature Converter with List Comprehensions
Create a program that:
- Converts list of Celsius temps to Fahrenheit using comprehension
- Filters out negative values in same comprehension
- Generates squared numbers for even indices only
"""

import random

class TemperatureConverter:
    """Temperature converter using list comprehensions"""
    
    def __init__(self):
        """Initialize the temperature converter"""
        self.celsius_temps = []
        self.converted_data = {}
    
    def generate_sample_data(self, count=15):
        """Generate sample temperature data"""
        # Generate random temperatures between -30 and 50 Celsius
        self.celsius_temps = [random.uniform(-30, 50) for _ in range(count)]
        print(f"Generated {count} sample temperatures: {[f'{temp:.1f}°C' for temp in self.celsius_temps]}")
    
    def convert_temperatures(self):
        """Convert Celsius to Fahrenheit using list comprehension"""
        if not self.celsius_temps:
            print("No temperatures to convert. Generate sample data first.")
            return
        
        print("\n=== Temperature Conversion Using List Comprehensions ===")
        
        # Step 1: Convert Celsius to Fahrenheit using comprehension
        print("1. Converting Celsius to Fahrenheit:")
        fahrenheit_temps = [(temp * 9/5) + 32 for temp in self.celsius_temps]
        print(f"   Celsius: {[f'{temp:.1f}°C' for temp in self.celsius_temps]}")
        print(f"   Fahrenheit: {[f'{temp:.1f}°F' for temp in fahrenheit_temps]}")
        
        # Step 2: Filter out negative values in same comprehension
        print("\n2. Filtering out negative values:")
        positive_fahrenheit = [temp for temp in fahrenheit_temps if temp > 32]
        print(f"   All Fahrenheit: {[f'{temp:.1f}°F' for temp in fahrenheit_temps]}")
        print(f"   Positive Fahrenheit: {[f'{temp:.1f}°F' for temp in positive_fahrenheit]}")
        print(f"   Removed {len(fahrenheit_temps) - len(positive_fahrenheit)} negative temperatures")
        
        # Step 3: Generate squared numbers for even indices only
        print("\n3. Squared numbers for even indices:")
        squared_even_indices = [i**2 for i in range(len(self.celsius_temps)) if i % 2 == 0]
        print(f"   Even indices: {list(range(0, len(self.celsius_temps), 2))}")
        print(f"   Squared values: {squared_even_indices}")
        
        # Store converted data
        self.converted_data = {
            'celsius': self.celsius_temps,
            'fahrenheit': fahrenheit_temps,
            'positive_fahrenheit': positive_fahrenheit,
            'squared_even_indices': squared_even_indices
        }
        
        return self.converted_data
    
    def demonstrate_conditional_comprehensions(self):
        """Demonstrate various conditional comprehensions"""
        if not self.celsius_temps:
            print("No temperatures to demonstrate.")
            return
        
        print("\n=== Conditional List Comprehensions ===")
        
        # Temperature categorization
        print("1. Temperature categorization:")
        cold_temps = [temp for temp in self.celsius_temps if temp < 0]
        mild_temps = [temp for temp in self.celsius_temps if 0 <= temp <= 20]
        warm_temps = [temp for temp in self.celsius_temps if temp > 20]
        
        print(f"   Cold (< 0°C): {[f'{temp:.1f}°C' for temp in cold_temps]}")
        print(f"   Mild (0-20°C): {[f'{temp:.1f}°C' for temp in mild_temps]}")
        print(f"   Warm (> 20°C): {[f'{temp:.1f}°C' for temp in warm_temps]}")
        
        # Temperature conversion with conditions
        print("\n2. Conditional temperature conversion:")
        # Convert to Fahrenheit but only for temperatures above -10°C
        warm_fahrenheit = [(temp * 9/5) + 32 for temp in self.celsius_temps if temp > -10]
        print(f"   Temperatures above -10°C converted to Fahrenheit: {[f'{temp:.1f}°F' for temp in warm_fahrenheit]}")
        
        # Temperature with labels
        print("\n3. Temperature with labels:")
        temp_labels = [f"{temp:.1f}°C ({'Cold' if temp < 0 else 'Mild' if temp <= 20 else 'Warm'})" 
                      for temp in self.celsius_temps]
        print(f"   Labeled temperatures: {temp_labels}")
    
    def demonstrate_nested_comprehensions(self):
        """Demonstrate nested list comprehensions"""
        if not self.celsius_temps:
            print("No temperatures to demonstrate.")
            return
        
        print("\n=== Nested List Comprehensions ===")
        
        # Create temperature ranges
        print("1. Temperature ranges:")
        # Create ranges around each temperature
        temp_ranges = [[temp - 2, temp, temp + 2] for temp in self.celsius_temps[:5]]
        print(f"   Temperature ranges: {temp_ranges}")
        
        # Flatten the ranges
        flattened_ranges = [temp for range_list in temp_ranges for temp in range_list]
        print(f"   Flattened ranges: {[f'{temp:.1f}°C' for temp in flattened_ranges]}")
        
        # Temperature conversion matrix
        print("\n2. Temperature conversion matrix:")
        # Create a matrix of different conversions
        conversions = ['Celsius', 'Fahrenheit', 'Kelvin']
        temp_matrix = [[temp, (temp * 9/5) + 32, temp + 273.15] for temp in self.celsius_temps[:3]]
        print(f"   Conversion matrix:")
        for i, row in enumerate(temp_matrix):
            print(f"   {conversions[i]}: {[f'{val:.1f}' for val in row]}")
    
    def demonstrate_practical_applications(self):
        """Demonstrate practical applications of list comprehensions"""
        if not self.celsius_temps:
            print("No temperatures to demonstrate.")
            return
        
        print("\n=== Practical Applications ===")
        
        # Weather forecasting simulation
        print("1. Weather forecasting simulation:")
        # Simulate temperature changes over time
        time_periods = ['Morning', 'Afternoon', 'Evening', 'Night']
        temp_forecast = [[temp + random.uniform(-5, 5) for _ in range(4)] for temp in self.celsius_temps[:3]]
        
        print("   Temperature forecast:")
        for i, temps in enumerate(temp_forecast):
            print(f"   Day {i+1}: {[f'{temp:.1f}°C' for temp in temps]}")
        
        # Find optimal temperatures
        print("\n2. Optimal temperature analysis:")
        # Find temperatures in comfortable range (18-24°C)
        comfortable_temps = [temp for temp in self.celsius_temps if 18 <= temp <= 24]
        print(f"   Comfortable temperatures (18-24°C): {[f'{temp:.1f}°C' for temp in comfortable_temps]}")
        
        # Temperature statistics
        print("\n3. Temperature statistics:")
        if self.celsius_temps:
            avg_temp = sum(self.celsius_temps) / len(self.celsius_temps)
            max_temp = max(self.celsius_temps)
            min_temp = min(self.celsius_temps)
            
            print(f"   Average: {avg_temp:.1f}°C")
            print(f"   Maximum: {max_temp:.1f}°C")
            print(f"   Minimum: {min_temp:.1f}°C")
    
    def compare_with_traditional_loops(self):
        """Compare list comprehensions with traditional loops"""
        if not self.celsius_temps:
            print("No temperatures to compare.")
            return
        
        print("\n=== List Comprehension vs Traditional Loops ===")
        
        # Conversion comparison
        print("1. Temperature conversion:")
        
        # List comprehension approach
        fahrenheit_comp = [(temp * 9/5) + 32 for temp in self.celsius_temps]
        
        # Traditional loop approach
        fahrenheit_loop = []
        for temp in self.celsius_temps:
            fahrenheit_loop.append((temp * 9/5) + 32)
        
        print(f"   List comprehension: {[f'{temp:.1f}°F' for temp in fahrenheit_comp[:5]]}")
        print(f"   Traditional loop: {[f'{temp:.1f}°F' for temp in fahrenheit_loop[:5]]}")
        print(f"   Results match: {fahrenheit_comp == fahrenheit_loop}")
        
        # Filtering comparison
        print("\n2. Filtering positive temperatures:")
        
        # List comprehension approach
        positive_comp = [temp for temp in self.celsius_temps if temp > 0]
        
        # Traditional loop approach
        positive_loop = []
        for temp in self.celsius_temps:
            if temp > 0:
                positive_loop.append(temp)
        
        print(f"   List comprehension: {[f'{temp:.1f}°C' for temp in positive_comp]}")
        print(f"   Traditional loop: {[f'{temp:.1f}°C' for temp in positive_loop]}")
        print(f"   Results match: {positive_comp == positive_loop}")
        
        # Squared even indices comparison
        print("\n3. Squared even indices:")
        
        # List comprehension approach
        squared_comp = [i**2 for i in range(len(self.celsius_temps)) if i % 2 == 0]
        
        # Traditional loop approach
        squared_loop = []
        for i in range(len(self.celsius_temps)):
            if i % 2 == 0:
                squared_loop.append(i**2)
        
        print(f"   List comprehension: {squared_comp}")
        print(f"   Traditional loop: {squared_loop}")
        print(f"   Results match: {squared_comp == squared_loop}")
    
    def display_statistics(self):
        """Display comprehensive statistics"""
        if not self.converted_data:
            print("No converted data available. Run convert_temperatures() first.")
            return
        
        data = self.converted_data
        
        print("\n=== Temperature Conversion Statistics ===")
        print(f"Total temperatures: {len(data['celsius'])}")
        print(f"Positive temperatures: {len(data['positive_fahrenheit'])}")
        print(f"Negative temperatures: {len(data['celsius']) - len(data['positive_fahrenheit'])}")
        
        if data['celsius']:
            avg_celsius = sum(data['celsius']) / len(data['celsius'])
            avg_fahrenheit = sum(data['fahrenheit']) / len(data['fahrenheit'])
            print(f"Average Celsius: {avg_celsius:.1f}°C")
            print(f"Average Fahrenheit: {avg_fahrenheit:.1f}°F")
        
        print(f"Squared even indices: {data['squared_even_indices']}")
        print(f"Sum of squared even indices: {sum(data['squared_even_indices'])}")

def main():
    """Main function to demonstrate the temperature converter"""
    print("=== List Comprehension Temperature Converter ===")
    converter = TemperatureConverter()
    
    while True:
        print("\nChoose an option:")
        print("1. Generate sample data")
        print("2. Convert temperatures")
        print("3. Demonstrate conditional comprehensions")
        print("4. Demonstrate nested comprehensions")
        print("5. Demonstrate practical applications")
        print("6. Compare with traditional loops")
        print("7. Display statistics")
        print("8. Exit")
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                try:
                    count = int(input("Enter number of temperatures to generate (default 15): ") or "15")
                    converter.generate_sample_data(count)
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '2':
                converter.convert_temperatures()
            
            elif choice == '3':
                converter.demonstrate_conditional_comprehensions()
            
            elif choice == '4':
                converter.demonstrate_nested_comprehensions()
            
            elif choice == '5':
                converter.demonstrate_practical_applications()
            
            elif choice == '6':
                converter.compare_with_traditional_loops()
            
            elif choice == '7':
                converter.display_statistics()
            
            elif choice == '8':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 8.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 