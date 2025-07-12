"""
Exercise 1: Data Processor
Create a data processor that:
- Converts list of Celsius temps to Fahrenheit using map
- Filters out negative temperatures using filter
- Calculates average temp using reduce
"""

from functools import reduce
import random

class DataProcessor:
    """Data processor using functional programming tools"""
    
    def __init__(self):
        """Initialize the data processor"""
        self.temperatures = []
        self.processed_data = {}
    
    def generate_sample_data(self, count=10):
        """Generate sample temperature data"""
        # Generate random temperatures between -20 and 40 Celsius
        self.temperatures = [random.uniform(-20, 40) for _ in range(count)]
        print(f"Generated {count} sample temperatures: {[f'{temp:.1f}°C' for temp in self.temperatures]}")
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32
    
    def is_positive_temperature(self, temp):
        """Check if temperature is positive"""
        return temp > 0
    
    def add_temperatures(self, a, b):
        """Add two temperatures for reduce operation"""
        return a + b
    
    def process_temperatures(self):
        """Process temperatures using functional programming tools"""
        if not self.temperatures:
            print("No temperatures to process. Generate sample data first.")
            return
        
        print("\n=== Processing Temperatures ===")
        
        # Step 1: Convert Celsius to Fahrenheit using map
        print("1. Converting Celsius to Fahrenheit using map():")
        fahrenheit_temps = list(map(self.celsius_to_fahrenheit, self.temperatures))
        print(f"   Celsius: {[f'{temp:.1f}°C' for temp in self.temperatures]}")
        print(f"   Fahrenheit: {[f'{temp:.1f}°F' for temp in fahrenheit_temps]}")
        
        # Step 2: Filter out negative temperatures using filter
        print("\n2. Filtering positive temperatures using filter():")
        positive_celsius = list(filter(self.is_positive_temperature, self.temperatures))
        positive_fahrenheit = list(filter(lambda x: x > 32, fahrenheit_temps))
        print(f"   Positive Celsius: {[f'{temp:.1f}°C' for temp in positive_celsius]}")
        print(f"   Positive Fahrenheit: {[f'{temp:.1f}°F' for temp in positive_fahrenheit]}")
        
        # Step 3: Calculate average using reduce
        print("\n3. Calculating averages using reduce():")
        if positive_celsius:
            avg_celsius = reduce(self.add_temperatures, positive_celsius) / len(positive_celsius)
            print(f"   Average Celsius: {avg_celsius:.1f}°C")
        else:
            avg_celsius = 0
            print("   No positive Celsius temperatures to average")
        
        if positive_fahrenheit:
            avg_fahrenheit = reduce(self.add_temperatures, positive_fahrenheit) / len(positive_fahrenheit)
            print(f"   Average Fahrenheit: {avg_fahrenheit:.1f}°F")
        else:
            avg_fahrenheit = 32
            print("   No positive Fahrenheit temperatures to average")
        
        # Store processed data
        self.processed_data = {
            'original_celsius': self.temperatures,
            'fahrenheit': fahrenheit_temps,
            'positive_celsius': positive_celsius,
            'positive_fahrenheit': positive_fahrenheit,
            'avg_celsius': avg_celsius,
            'avg_fahrenheit': avg_fahrenheit
        }
        
        return self.processed_data
    
    def analyze_temperature_ranges(self):
        """Analyze temperature ranges using functional programming"""
        if not self.temperatures:
            print("No temperatures to analyze.")
            return
        
        print("\n=== Temperature Range Analysis ===")
        
        # Find temperature ranges using functional programming
        cold_temps = list(filter(lambda x: x < 0, self.temperatures))
        mild_temps = list(filter(lambda x: 0 <= x <= 20, self.temperatures))
        warm_temps = list(filter(lambda x: x > 20, self.temperatures))
        
        print(f"Cold temperatures (< 0°C): {len(cold_temps)} temps")
        if cold_temps:
            coldest = reduce(lambda a, b: a if a < b else b, cold_temps)
            print(f"   Coldest: {coldest:.1f}°C")
        
        print(f"Mild temperatures (0-20°C): {len(mild_temps)} temps")
        if mild_temps:
            avg_mild = reduce(self.add_temperatures, mild_temps) / len(mild_temps)
            print(f"   Average mild: {avg_mild:.1f}°C")
        
        print(f"Warm temperatures (> 20°C): {len(warm_temps)} temps")
        if warm_temps:
            warmest = reduce(lambda a, b: a if a > b else b, warm_temps)
            print(f"   Warmest: {warmest:.1f}°C")
    
    def demonstrate_lambda_functions(self):
        """Demonstrate various lambda functions with temperature data"""
        if not self.temperatures:
            print("No temperatures to demonstrate.")
            return
        
        print("\n=== Lambda Function Demonstrations ===")
        
        # Lambda with map
        print("1. Lambda with map() - Convert to Kelvin:")
        kelvin_temps = list(map(lambda c: c + 273.15, self.temperatures))
        print(f"   Kelvin: {[f'{temp:.1f}K' for temp in kelvin_temps]}")
        
        # Lambda with filter
        print("\n2. Lambda with filter() - Find temperatures above 15°C:")
        above_15 = list(filter(lambda x: x > 15, self.temperatures))
        print(f"   Above 15°C: {[f'{temp:.1f}°C' for temp in above_15]}")
        
        # Lambda with reduce
        print("\n3. Lambda with reduce() - Find temperature range:")
        temp_range = reduce(lambda a, b: max(a, b) - min(a, b), self.temperatures)
        print(f"   Temperature range: {temp_range:.1f}°C")
        
        # Complex lambda operations
        print("\n4. Complex lambda operations:")
        # Convert to Fahrenheit and filter positive, then find max
        positive_fahrenheit = list(filter(lambda x: x > 32, 
                                        map(self.celsius_to_fahrenheit, self.temperatures)))
        if positive_fahrenheit:
            max_positive_f = reduce(lambda a, b: a if a > b else b, positive_fahrenheit)
            print(f"   Max positive Fahrenheit: {max_positive_f:.1f}°F")
    
    def compare_with_list_comprehensions(self):
        """Compare functional programming with list comprehensions"""
        if not self.temperatures:
            print("No temperatures to compare.")
            return
        
        print("\n=== Functional vs List Comprehension Comparison ===")
        
        # Map vs List Comprehension
        print("1. Celsius to Fahrenheit conversion:")
        # Functional approach
        fahrenheit_func = list(map(self.celsius_to_fahrenheit, self.temperatures))
        # List comprehension approach
        fahrenheit_comp = [self.celsius_to_fahrenheit(temp) for temp in self.temperatures]
        print(f"   Functional (map): {[f'{temp:.1f}°F' for temp in fahrenheit_func]}")
        print(f"   List comprehension: {[f'{temp:.1f}°F' for temp in fahrenheit_comp]}")
        print(f"   Results match: {fahrenheit_func == fahrenheit_comp}")
        
        # Filter vs List Comprehension
        print("\n2. Filtering positive temperatures:")
        # Functional approach
        positive_func = list(filter(self.is_positive_temperature, self.temperatures))
        # List comprehension approach
        positive_comp = [temp for temp in self.temperatures if temp > 0]
        print(f"   Functional (filter): {[f'{temp:.1f}°C' for temp in positive_func]}")
        print(f"   List comprehension: {[f'{temp:.1f}°C' for temp in positive_comp]}")
        print(f"   Results match: {positive_func == positive_comp}")
        
        # Reduce vs sum()
        print("\n3. Calculating sum:")
        # Functional approach
        sum_func = reduce(self.add_temperatures, self.temperatures)
        # Built-in sum approach
        sum_builtin = sum(self.temperatures)
        print(f"   Functional (reduce): {sum_func:.1f}")
        print(f"   Built-in sum(): {sum_builtin:.1f}")
        print(f"   Results match: {abs(sum_func - sum_builtin) < 0.001}")
    
    def display_statistics(self):
        """Display comprehensive statistics"""
        if not self.processed_data:
            print("No processed data available. Run process_temperatures() first.")
            return
        
        print("\n=== Data Processing Statistics ===")
        data = self.processed_data
        
        print(f"Original temperatures: {len(data['original_celsius'])}")
        print(f"Positive temperatures: {len(data['positive_celsius'])}")
        print(f"Negative temperatures: {len(data['original_celsius']) - len(data['positive_celsius'])}")
        print(f"Average Celsius: {data['avg_celsius']:.1f}°C")
        print(f"Average Fahrenheit: {data['avg_fahrenheit']:.1f}°F")
        
        if data['original_celsius']:
            min_temp = min(data['original_celsius'])
            max_temp = max(data['original_celsius'])
            print(f"Temperature range: {min_temp:.1f}°C to {max_temp:.1f}°C")

def main():
    """Main function to demonstrate the data processor"""
    print("=== Functional Programming Data Processor ===")
    processor = DataProcessor()
    
    while True:
        print("\nChoose an option:")
        print("1. Generate sample data")
        print("2. Process temperatures")
        print("3. Analyze temperature ranges")
        print("4. Demonstrate lambda functions")
        print("5. Compare with list comprehensions")
        print("6. Display statistics")
        print("7. Exit")
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                try:
                    count = int(input("Enter number of temperatures to generate (default 10): ") or "10")
                    processor.generate_sample_data(count)
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '2':
                processor.process_temperatures()
            
            elif choice == '3':
                processor.analyze_temperature_ranges()
            
            elif choice == '4':
                processor.demonstrate_lambda_functions()
            
            elif choice == '5':
                processor.compare_with_list_comprehensions()
            
            elif choice == '6':
                processor.display_statistics()
            
            elif choice == '7':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 7.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 