"""
Exercise 2: File Reader
Build a file reader that:
- Gracefully handles missing files
- Shows different messages for different error types
- Always closes file resources
"""

import os
from datetime import datetime

class FileReader:
    def __init__(self):
        """Initialize the file reader"""
        self.read_attempts = 0
        self.successful_reads = 0
        self.failed_reads = 0
    
    def read_file_safe(self, filename):
        """
        Safely read a file with comprehensive error handling
        
        Args:
            filename (str): Path to the file to read
        
        Returns:
            str: File contents or None if failed
        """
        file_handle = None
        self.read_attempts += 1
        
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"❌ File '{filename}' does not exist.")
                self.failed_reads += 1
                return None
            
            # Check if it's a file (not a directory)
            if not os.path.isfile(filename):
                print(f"❌ '{filename}' is not a file (it might be a directory).")
                self.failed_reads += 1
                return None
            
            # Check file permissions
            if not os.access(filename, os.R_OK):
                print(f"❌ No permission to read file '{filename}'.")
                self.failed_reads += 1
                return None
            
            # Open and read the file
            file_handle = open(filename, 'r', encoding='utf-8')
            content = file_handle.read()
            
            print(f"✅ Successfully read '{filename}' ({len(content)} characters)")
            self.successful_reads += 1
            return content
            
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found.")
            self.failed_reads += 1
            return None
            
        except PermissionError:
            print(f"❌ Permission denied: Cannot read '{filename}'.")
            self.failed_reads += 1
            return None
            
        except UnicodeDecodeError as e:
            print(f"❌ Encoding error in '{filename}': {e}")
            print("   Try reading with a different encoding.")
            self.failed_reads += 1
            return None
            
        except IsADirectoryError:
            print(f"❌ '{filename}' is a directory, not a file.")
            self.failed_reads += 1
            return None
            
        except OSError as e:
            print(f"❌ Operating system error reading '{filename}': {e}")
            self.failed_reads += 1
            return None
            
        except Exception as e:
            print(f"❌ Unexpected error reading '{filename}': {e}")
            self.failed_reads += 1
            return None
            
        finally:
            # Always close the file handle if it was opened
            if file_handle is not None:
                try:
                    file_handle.close()
                    print(f"🔒 File '{filename}' closed successfully.")
                except Exception as e:
                    print(f"⚠️  Warning: Error closing file '{filename}': {e}")
    
    def read_file_lines(self, filename):
        """
        Read a file line by line with error handling
        
        Args:
            filename (str): Path to the file to read
        
        Returns:
            list: List of lines or empty list if failed
        """
        lines = []
        file_handle = None
        self.read_attempts += 1
        
        try:
            if not os.path.exists(filename):
                print(f"❌ File '{filename}' does not exist.")
                self.failed_reads += 1
                return []
            
            file_handle = open(filename, 'r', encoding='utf-8')
            
            for line_num, line in enumerate(file_handle, 1):
                try:
                    lines.append(line.rstrip('\n'))
                except UnicodeDecodeError:
                    print(f"⚠️  Warning: Line {line_num} has encoding issues, skipping...")
                    continue
            
            print(f"✅ Successfully read '{filename}' ({len(lines)} lines)")
            self.successful_reads += 1
            return lines
            
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found.")
            self.failed_reads += 1
            return []
            
        except PermissionError:
            print(f"❌ Permission denied: Cannot read '{filename}'.")
            self.failed_reads += 1
            return []
            
        except Exception as e:
            print(f"❌ Error reading '{filename}': {e}")
            self.failed_reads += 1
            return []
            
        finally:
            if file_handle is not None:
                try:
                    file_handle.close()
                    print(f"🔒 File '{filename}' closed successfully.")
                except Exception as e:
                    print(f"⚠️  Warning: Error closing file '{filename}': {e}")
    
    def create_sample_file(self, filename, content):
        """
        Create a sample file for testing
        
        Args:
            filename (str): Name of the file to create
            content (str): Content to write to the file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ Created sample file: {filename}")
        except Exception as e:
            print(f"❌ Error creating sample file '{filename}': {e}")
    
    def get_statistics(self):
        """Get reading statistics"""
        return {
            'total_attempts': self.read_attempts,
            'successful_reads': self.successful_reads,
            'failed_reads': self.failed_reads,
            'success_rate': (self.successful_reads / self.read_attempts * 100) if self.read_attempts > 0 else 0
        }
    
    def display_statistics(self):
        """Display reading statistics"""
        stats = self.get_statistics()
        print(f"\n=== File Reading Statistics ===")
        print(f"Total attempts: {stats['total_attempts']}")
        print(f"Successful reads: {stats['successful_reads']}")
        print(f"Failed reads: {stats['failed_reads']}")
        print(f"Success rate: {stats['success_rate']:.1f}%")

def demonstrate_file_reader():
    """Demonstrate the file reader with various scenarios"""
    print("=== File Reader Demo ===")
    reader = FileReader()
    
    # Create sample files
    sample_content = """This is a sample file.
It contains multiple lines.
Each line demonstrates file reading.
This file will be used for testing."""
    
    reader.create_sample_file("sample.txt", sample_content)
    reader.create_sample_file("empty.txt", "")
    
    print("\n1. Reading existing file:")
    content = reader.read_file_safe("sample.txt")
    if content:
        print(f"Content preview: {content[:50]}...")
    
    print("\n2. Reading empty file:")
    content = reader.read_file_safe("empty.txt")
    if content is not None:
        print(f"Empty file content: '{content}'")
    
    print("\n3. Reading non-existent file:")
    reader.read_file_safe("nonexistent.txt")
    
    print("\n4. Reading file line by line:")
    lines = reader.read_file_lines("sample.txt")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}")
    
    print("\n5. Trying to read a directory:")
    reader.read_file_safe(".")
    
    # Display statistics
    reader.display_statistics()

def main():
    """Main function to run the file reader"""
    print("=== File Reader ===")
    reader = FileReader()
    
    while True:
        print("\nChoose an option:")
        print("1. Read a file")
        print("2. Read file line by line")
        print("3. Create sample file")
        print("4. Run demo")
        print("5. Show statistics")
        print("6. Exit")
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                filename = input("Enter filename to read: ").strip()
                content = reader.read_file_safe(filename)
                if content:
                    print(f"\nFile content:\n{content}")
            
            elif choice == '2':
                filename = input("Enter filename to read line by line: ").strip()
                lines = reader.read_file_lines(filename)
                if lines:
                    print(f"\nFile lines:")
                    for i, line in enumerate(lines, 1):
                        print(f"{i:2d}: {line}")
            
            elif choice == '3':
                filename = input("Enter filename to create: ").strip()
                content = input("Enter file content: ")
                reader.create_sample_file(filename, content)
            
            elif choice == '4':
                demonstrate_file_reader()
            
            elif choice == '5':
                reader.display_statistics()
            
            elif choice == '6':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 6.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 