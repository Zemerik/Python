"""
Exercise 1: Name Processor
Create a program that:
- Reads a text file containing names
- Writes capitalized names to a new file
- Appends a timestamp to the end
"""

import os
from datetime import datetime

class NameProcessor:
    def __init__(self):
        """Initialize the name processor"""
        self.input_file = "names.txt"
        self.output_file = "capitalized_names.txt"
    
    def create_sample_file(self):
        """Create a sample input file with names"""
        sample_names = [
            "alice johnson",
            "bob smith",
            "charlie brown",
            "diana prince",
            "eve wilson",
            "frank miller",
            "grace lee",
            "henry davis",
            "ivy chen",
            "jack taylor"
        ]
        
        try:
            with open(self.input_file, 'w') as file:
                for name in sample_names:
                    file.write(name + '\n')
            print(f"Created sample file: {self.input_file}")
        except Exception as e:
            print(f"Error creating sample file: {e}")
    
    def read_names_from_file(self):
        """Read names from the input file"""
        names = []
        try:
            with open(self.input_file, 'r') as file:
                for line in file:
                    name = line.strip()
                    if name:  # Skip empty lines
                        names.append(name)
            print(f"Read {len(names)} names from {self.input_file}")
            return names
        except FileNotFoundError:
            print(f"File {self.input_file} not found. Creating sample file...")
            self.create_sample_file()
            return self.read_names_from_file()
        except Exception as e:
            print(f"Error reading file: {e}")
            return []
    
    def capitalize_names(self, names):
        """Capitalize all names"""
        capitalized_names = []
        for name in names:
            # Capitalize each word in the name
            capitalized_name = ' '.join(word.capitalize() for word in name.split())
            capitalized_names.append(capitalized_name)
        return capitalized_names
    
    def write_capitalized_names(self, capitalized_names):
        """Write capitalized names to output file"""
        try:
            with open(self.output_file, 'w') as file:
                for name in capitalized_names:
                    file.write(name + '\n')
            print(f"Wrote {len(capitalized_names)} capitalized names to {self.output_file}")
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False
    
    def append_timestamp(self):
        """Append timestamp to the output file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.output_file, 'a') as file:
                file.write(f"\nProcessed on: {timestamp}\n")
            print(f"Appended timestamp: {timestamp}")
            return True
        except Exception as e:
            print(f"Error appending timestamp: {e}")
            return False
    
    def display_file_contents(self, filename):
        """Display the contents of a file"""
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\n=== Contents of {filename} ===")
                print(content)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    def process_names(self):
        """Main processing function"""
        print("=== Name Processor ===")
        
        # Read names from input file
        names = self.read_names_from_file()
        if not names:
            print("No names to process.")
            return
        
        # Display original names
        print(f"\nOriginal names: {names}")
        
        # Capitalize names
        capitalized_names = self.capitalize_names(names)
        print(f"Capitalized names: {capitalized_names}")
        
        # Write to output file
        if self.write_capitalized_names(capitalized_names):
            # Append timestamp
            self.append_timestamp()
            
            # Display results
            print(f"\nProcessing complete!")
            self.display_file_contents(self.output_file)
        else:
            print("Failed to write output file.")

def main():
    processor = NameProcessor()
    
    while True:
        print("\n=== Name Processor Menu ===")
        print("1. Process names")
        print("2. View input file")
        print("3. View output file")
        print("4. Create new sample file")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                processor.process_names()
            
            elif choice == 2:
                processor.display_file_contents(processor.input_file)
            
            elif choice == 3:
                processor.display_file_contents(processor.output_file)
            
            elif choice == 4:
                processor.create_sample_file()
            
            elif choice == 5:
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 