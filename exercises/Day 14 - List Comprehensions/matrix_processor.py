"""
Exercise 2: Matrix Processor
Build a matrix processor that:
- Flattens 2D list using nested comprehension
- Transposes matrix rows/columns
- Creates multiplication table using nested loops
"""

import random

class MatrixProcessor:
    """Matrix processor using list comprehensions"""
    
    def __init__(self):
        """Initialize the matrix processor"""
        self.matrix = []
        self.processed_data = {}
    
    def generate_sample_matrix(self, rows=4, cols=4):
        """Generate sample matrix with random numbers"""
        self.matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]
        print(f"Generated {rows}x{cols} matrix:")
        self.display_matrix(self.matrix)
    
    def display_matrix(self, matrix, title="Matrix"):
        """Display a matrix in a formatted way"""
        print(f"\n{title}:")
        for row in matrix:
            print(f"  {row}")
    
    def flatten_matrix(self):
        """Flatten 2D list using nested comprehension"""
        if not self.matrix:
            print("No matrix to flatten. Generate sample matrix first.")
            return
        
        print("\n=== Matrix Flattening Using Nested Comprehension ===")
        
        # Method 1: Simple flattening
        print("1. Simple flattening:")
        flattened = [element for row in self.matrix for element in row]
        print(f"   Original matrix: {self.matrix}")
        print(f"   Flattened: {flattened}")
        
        # Method 2: Flattening with conditions
        print("\n2. Flattening with conditions (even numbers only):")
        flattened_even = [element for row in self.matrix for element in row if element % 2 == 0]
        print(f"   Even numbers: {flattened_even}")
        
        # Method 3: Flattening with transformation
        print("\n3. Flattening with transformation (squared values):")
        flattened_squared = [element**2 for row in self.matrix for element in row]
        print(f"   Squared values: {flattened_squared}")
        
        # Store flattened data
        self.processed_data['flattened'] = {
            'simple': flattened,
            'even_only': flattened_even,
            'squared': flattened_squared
        }
        
        return self.processed_data['flattened']
    
    def transpose_matrix(self):
        """Transpose matrix rows/columns using list comprehension"""
        if not self.matrix:
            print("No matrix to transpose. Generate sample matrix first.")
            return
        
        print("\n=== Matrix Transposition ===")
        
        # Method 1: Using nested comprehension
        print("1. Transposition using nested comprehension:")
        rows, cols = len(self.matrix), len(self.matrix[0])
        transposed = [[self.matrix[i][j] for i in range(rows)] for j in range(cols)]
        
        print("   Original matrix:")
        self.display_matrix(self.matrix, "Original")
        print("   Transposed matrix:")
        self.display_matrix(transposed, "Transposed")
        
        # Method 2: Using zip (alternative approach)
        print("\n2. Transposition using zip:")
        transposed_zip = list(map(list, zip(*self.matrix)))
        self.display_matrix(transposed_zip, "Transposed (zip)")
        
        # Verify both methods give same result
        print(f"   Methods match: {transposed == transposed_zip}")
        
        # Store transposed data
        self.processed_data['transposed'] = {
            'comprehension': transposed,
            'zip_method': transposed_zip
        }
        
        return self.processed_data['transposed']
    
    def create_multiplication_table(self, size=10):
        """Create multiplication table using nested loops"""
        print(f"\n=== Multiplication Table ({size}x{size}) ===")
        
        # Create multiplication table using nested comprehension
        multiplication_table = [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
        
        print("Multiplication table:")
        # Display with proper formatting
        for i, row in enumerate(multiplication_table):
            formatted_row = [f"{val:3}" for val in row]
            print(f"  {formatted_row}")
        
        # Store multiplication table
        self.processed_data['multiplication_table'] = multiplication_table
        
        return multiplication_table
    
    def demonstrate_advanced_operations(self):
        """Demonstrate advanced matrix operations using comprehensions"""
        if not self.matrix:
            print("No matrix to demonstrate. Generate sample matrix first.")
            return
        
        print("\n=== Advanced Matrix Operations ===")
        
        # Row and column sums
        print("1. Row and column sums:")
        row_sums = [sum(row) for row in self.matrix]
        col_sums = [sum(self.matrix[i][j] for i in range(len(self.matrix))) 
                   for j in range(len(self.matrix[0]))]
        
        print(f"   Row sums: {row_sums}")
        print(f"   Column sums: {col_sums}")
        
        # Diagonal elements
        print("\n2. Diagonal elements:")
        main_diagonal = [self.matrix[i][i] for i in range(min(len(self.matrix), len(self.matrix[0])))]
        anti_diagonal = [self.matrix[i][len(self.matrix[0])-1-i] 
                        for i in range(min(len(self.matrix), len(self.matrix[0])))]
        
        print(f"   Main diagonal: {main_diagonal}")
        print(f"   Anti-diagonal: {anti_diagonal}")
        
        # Matrix statistics
        print("\n3. Matrix statistics:")
        all_elements = [element for row in self.matrix for element in row]
        if all_elements:
            avg_value = sum(all_elements) / len(all_elements)
            max_value = max(all_elements)
            min_value = min(all_elements)
            
            print(f"   Average: {avg_value:.2f}")
            print(f"   Maximum: {max_value}")
            print(f"   Minimum: {min_value}")
        
        # Store advanced operations data
        self.processed_data['advanced'] = {
            'row_sums': row_sums,
            'col_sums': col_sums,
            'main_diagonal': main_diagonal,
            'anti_diagonal': anti_diagonal
        }
    
    def demonstrate_conditional_matrix_operations(self):
        """Demonstrate conditional matrix operations"""
        if not self.matrix:
            print("No matrix to demonstrate. Generate sample matrix first.")
            return
        
        print("\n=== Conditional Matrix Operations ===")
        
        # Filter elements greater than 10
        print("1. Elements greater than 10:")
        large_elements = [element for row in self.matrix for element in row if element > 10]
        print(f"   Large elements: {large_elements}")
        
        # Create matrix with only even numbers (0 for odd)
        print("\n2. Matrix with even numbers only:")
        even_matrix = [[element if element % 2 == 0 else 0 for element in row] for row in self.matrix]
        self.display_matrix(even_matrix, "Even numbers only")
        
        # Create matrix with conditional formatting
        print("\n3. Matrix with conditional formatting:")
        formatted_matrix = [['*' if element > 10 else str(element) for element in row] for row in self.matrix]
        self.display_matrix(formatted_matrix, "Conditional formatting")
        
        # Find positions of specific values
        print("\n4. Positions of values greater than 15:")
        positions = [(i, j) for i, row in enumerate(self.matrix) 
                    for j, element in enumerate(row) if element > 15]
        print(f"   Positions: {positions}")
    
    def demonstrate_nested_comprehensions(self):
        """Demonstrate various nested comprehensions"""
        if not self.matrix:
            print("No matrix to demonstrate. Generate sample matrix first.")
            return
        
        print("\n=== Nested Comprehension Demonstrations ===")
        
        # Create identity matrix
        print("1. Identity matrix:")
        size = min(len(self.matrix), len(self.matrix[0]))
        identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
        self.display_matrix(identity, "Identity Matrix")
        
        # Create matrix with row and column indices
        print("\n2. Matrix with indices:")
        index_matrix = [[f"({i},{j})" for j in range(len(self.matrix[0]))] 
                       for i in range(len(self.matrix))]
        self.display_matrix(index_matrix, "Index Matrix")
        
        # Create matrix with alternating values
        print("\n3. Alternating matrix:")
        alternating = [[1 if (i + j) % 2 == 0 else 0 
                       for j in range(len(self.matrix[0]))] 
                      for i in range(len(self.matrix))]
        self.display_matrix(alternating, "Alternating Matrix")
        
        # Create matrix with cumulative row sums
        print("\n4. Cumulative row sums:")
        cumulative = [[sum(row[:j+1]) for j in range(len(row))] for row in self.matrix]
        self.display_matrix(cumulative, "Cumulative Row Sums")
    
    def compare_with_traditional_loops(self):
        """Compare list comprehensions with traditional loops"""
        if not self.matrix:
            print("No matrix to compare. Generate sample matrix first.")
            return
        
        print("\n=== List Comprehension vs Traditional Loops ===")
        
        # Flattening comparison
        print("1. Matrix flattening:")
        
        # List comprehension approach
        flattened_comp = [element for row in self.matrix for element in row]
        
        # Traditional loop approach
        flattened_loop = []
        for row in self.matrix:
            for element in row:
                flattened_loop.append(element)
        
        print(f"   List comprehension: {flattened_comp}")
        print(f"   Traditional loop: {flattened_loop}")
        print(f"   Results match: {flattened_comp == flattened_loop}")
        
        # Transposition comparison
        print("\n2. Matrix transposition:")
        
        # List comprehension approach
        rows, cols = len(self.matrix), len(self.matrix[0])
        transposed_comp = [[self.matrix[i][j] for i in range(rows)] for j in range(cols)]
        
        # Traditional loop approach
        transposed_loop = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(self.matrix[i][j])
            transposed_loop.append(new_row)
        
        print(f"   List comprehension: {transposed_comp}")
        print(f"   Traditional loop: {transposed_loop}")
        print(f"   Results match: {transposed_comp == transposed_loop}")
        
        # Row sums comparison
        print("\n3. Row sums calculation:")
        
        # List comprehension approach
        row_sums_comp = [sum(row) for row in self.matrix]
        
        # Traditional loop approach
        row_sums_loop = []
        for row in self.matrix:
            row_sum = 0
            for element in row:
                row_sum += element
            row_sums_loop.append(row_sum)
        
        print(f"   List comprehension: {row_sums_comp}")
        print(f"   Traditional loop: {row_sums_loop}")
        print(f"   Results match: {row_sums_comp == row_sums_loop}")
    
    def display_statistics(self):
        """Display comprehensive matrix statistics"""
        if not self.processed_data:
            print("No processed data available. Run matrix operations first.")
            return
        
        print("\n=== Matrix Processing Statistics ===")
        
        if 'flattened' in self.processed_data:
            data = self.processed_data['flattened']
            print(f"Flattened elements: {len(data['simple'])}")
            print(f"Even elements: {len(data['even_only'])}")
            print(f"Sum of all elements: {sum(data['simple'])}")
            print(f"Sum of even elements: {sum(data['even_only'])}")
        
        if 'advanced' in self.processed_data:
            data = self.processed_data['advanced']
            print(f"Row sums: {data['row_sums']}")
            print(f"Column sums: {data['col_sums']}")
            print(f"Main diagonal sum: {sum(data['main_diagonal'])}")
            print(f"Anti-diagonal sum: {sum(data['anti_diagonal'])}")
        
        if 'multiplication_table' in self.processed_data:
            table = self.processed_data['multiplication_table']
            print(f"Multiplication table size: {len(table)}x{len(table[0])}")
            print(f"Largest value in table: {max(max(row) for row in table)}")

def main():
    """Main function to demonstrate the matrix processor"""
    print("=== List Comprehension Matrix Processor ===")
    processor = MatrixProcessor()
    
    while True:
        print("\nChoose an option:")
        print("1. Generate sample matrix")
        print("2. Flatten matrix")
        print("3. Transpose matrix")
        print("4. Create multiplication table")
        print("5. Advanced operations")
        print("6. Conditional operations")
        print("7. Nested comprehensions")
        print("8. Compare with traditional loops")
        print("9. Display statistics")
        print("10. Exit")
        
        try:
            choice = input("Enter your choice (1-10): ").strip()
            
            if choice == '1':
                try:
                    rows = int(input("Enter number of rows (default 4): ") or "4")
                    cols = int(input("Enter number of columns (default 4): ") or "4")
                    processor.generate_sample_matrix(rows, cols)
                except ValueError:
                    print("Please enter valid numbers.")
            
            elif choice == '2':
                processor.flatten_matrix()
            
            elif choice == '3':
                processor.transpose_matrix()
            
            elif choice == '4':
                try:
                    size = int(input("Enter table size (default 10): ") or "10")
                    processor.create_multiplication_table(size)
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '5':
                processor.demonstrate_advanced_operations()
            
            elif choice == '6':
                processor.demonstrate_conditional_matrix_operations()
            
            elif choice == '7':
                processor.demonstrate_nested_comprehensions()
            
            elif choice == '8':
                processor.compare_with_traditional_loops()
            
            elif choice == '9':
                processor.display_statistics()
            
            elif choice == '10':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 10.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 