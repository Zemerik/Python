"""
Exercise 2: Multiplication Table Generator
Build a multiplication table generator that:
- Takes an integer input N
- Prints tables from 1x1 to NxN
- Formats output in rows and columns
"""


def get_table_size():
    """Get the size of multiplication table from user"""
    while True:
        try:
            n = int(input("Enter the size of multiplication table (1-12): "))
            if 1 <= n <= 12:
                return n
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")


def generate_multiplication_table(n):
    """Generate multiplication table from 1x1 to NxN"""
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table


def format_table_header(n):
    """Format the header row of the table"""
    header = "   "  # Space for row labels
    for j in range(1, n + 1):
        header += f"{j:4}"
    return header


def format_table_row(row_num, row_data):
    """Format a single row of the table"""
    row_str = f"{row_num:2} "  # Row label
    for value in row_data:
        row_str += f"{value:4}"
    return row_str


def display_multiplication_table(table):
    """Display the formatted multiplication table"""
    n = len(table)
    
    print("\n=== Multiplication Table ===")
    print(format_table_header(n))
    print("-" * (4 * n + 3))  # Separator line
    
    for i, row in enumerate(table, 1):
        print(format_table_row(i, row))


def display_individual_tables(n):
    """Display individual multiplication tables for each number"""
    print(f"\n=== Individual Tables (1 to {n}) ===")
    
    for i in range(1, n + 1):
        print(f"\nTable of {i}:")
        print("-" * 20)
        for j in range(1, 11):  # Show first 10 multiples
            print(f"{i} x {j:2} = {i * j:3}")


def main():
    print("=== Multiplication Table Generator ===")
    
    # Get table size from user
    n = get_table_size()
    
    # Generate the table
    table = generate_multiplication_table(n)
    
    # Display the complete table
    display_multiplication_table(table)
    
    # Display individual tables
    display_individual_tables(n)
    
    print(f"\nGenerated multiplication tables from 1x1 to {n}x{n}")

if __name__ == "__main__":
    main() 