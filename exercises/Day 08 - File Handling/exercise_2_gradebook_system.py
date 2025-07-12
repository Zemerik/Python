"""
Exercise 2: Gradebook System
Build a gradebook system that:
- Stores student records in CSV format
- Reads existing grades
- Allows adding new entries
- Calculates class average
"""

import csv
import os
from datetime import datetime

class GradebookSystem:
    def __init__(self, filename="gradebook.csv"):
        """Initialize the gradebook system"""
        self.filename = filename
        self.headers = ['Student Name', 'Math', 'Science', 'English', 'History', 'Date Added']
    
    def create_sample_gradebook(self):
        """Create a sample gradebook with initial data"""
        sample_data = [
            ['Alice Johnson', 85, 92, 88, 90, '2024-01-15'],
            ['Bob Smith', 78, 88, 82, 85, '2024-01-15'],
            ['Charlie Brown', 92, 85, 90, 87, '2024-01-15'],
            ['Diana Prince', 95, 90, 94, 92, '2024-01-15'],
            ['Eve Wilson', 88, 87, 85, 89, '2024-01-15']
        ]
        
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                writer.writerows(sample_data)
            print(f"Created sample gradebook: {self.filename}")
        except Exception as e:
            print(f"Error creating sample gradebook: {e}")
    
    def read_gradebook(self):
        """Read existing grades from CSV file"""
        students = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
            print(f"Read {len(students)} student records from {self.filename}")
            return students
        except FileNotFoundError:
            print(f"Gradebook {self.filename} not found. Creating sample gradebook...")
            self.create_sample_gradebook()
            return self.read_gradebook()
        except Exception as e:
            print(f"Error reading gradebook: {e}")
            return []
    
    def add_student(self, name, math, science, english, history):
        """Add a new student entry to the gradebook"""
        try:
            # Read existing data
            students = self.read_gradebook()
            
            # Add new student
            new_student = {
                'Student Name': name,
                'Math': math,
                'Science': science,
                'English': english,
                'History': history,
                'Date Added': datetime.now().strftime('%Y-%m-%d')
            }
            students.append(new_student)
            
            # Write back to file
            with open(self.filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(students)
            
            print(f"Added student: {name}")
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False
    
    def calculate_class_averages(self):
        """Calculate class averages for each subject"""
        students = self.read_gradebook()
        if not students:
            return {}
        
        subjects = ['Math', 'Science', 'English', 'History']
        averages = {}
        
        for subject in subjects:
            scores = []
            for student in students:
                try:
                    score = int(student[subject])
                    scores.append(score)
                except (ValueError, KeyError):
                    continue
            
            if scores:
                average = sum(scores) / len(scores)
                averages[subject] = round(average, 2)
            else:
                averages[subject] = 0
        
        return averages
    
    def find_top_student(self, subject):
        """Find the top student in a specific subject"""
        students = self.read_gradebook()
        if not students:
            return None
        
        top_student = None
        top_score = -1
        
        for student in students:
            try:
                score = int(student[subject])
                if score > top_score:
                    top_score = score
                    top_student = student
            except (ValueError, KeyError):
                continue
        
        return top_student, top_score
    
    def display_gradebook(self):
        """Display the complete gradebook"""
        students = self.read_gradebook()
        if not students:
            print("No students in gradebook.")
            return
        
        print(f"\n=== Gradebook ({len(students)} students) ===")
        print(f"{'Name':<20} {'Math':<6} {'Science':<8} {'English':<8} {'History':<8} {'Date':<12}")
        print("-" * 70)
        
        for student in students:
            name = student['Student Name'][:19]  # Truncate long names
            math = student.get('Math', 'N/A')
            science = student.get('Science', 'N/A')
            english = student.get('English', 'N/A')
            history = student.get('History', 'N/A')
            date = student.get('Date Added', 'N/A')
            
            print(f"{name:<20} {math:<6} {science:<8} {english:<8} {history:<8} {date:<12}")
    
    def display_statistics(self):
        """Display class statistics"""
        print("\n=== Class Statistics ===")
        
        # Calculate averages
        averages = self.calculate_class_averages()
        for subject, average in averages.items():
            print(f"{subject} Average: {average}")
        
        # Find top students
        subjects = ['Math', 'Science', 'English', 'History']
        print("\n=== Top Students ===")
        for subject in subjects:
            top_student, top_score = self.find_top_student(subject)
            if top_student:
                print(f"{subject}: {top_student['Student Name']} ({top_score})")
        
        # Calculate overall class average
        if averages:
            overall_average = sum(averages.values()) / len(averages)
            print(f"\nOverall Class Average: {overall_average:.2f}")

def get_student_input():
    """Get new student information from user"""
    name = input("Enter student name: ").strip()
    
    while True:
        try:
            math = int(input("Enter math score (0-100): "))
            if 0 <= math <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            science = int(input("Enter science score (0-100): "))
            if 0 <= science <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            english = int(input("Enter english score (0-100): "))
            if 0 <= english <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            history = int(input("Enter history score (0-100): "))
            if 0 <= history <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    return name, math, science, english, history

def display_menu():
    """Display the main menu"""
    print("\n=== Gradebook System Menu ===")
    print("1. View gradebook")
    print("2. Add new student")
    print("3. View class statistics")
    print("4. Create sample gradebook")
    print("5. Exit")

def main():
    print("=== Gradebook System ===")
    gradebook = GradebookSystem()
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                gradebook.display_gradebook()
            
            elif choice == 2:
                name, math, science, english, history = get_student_input()
                gradebook.add_student(name, math, science, english, history)
            
            elif choice == 3:
                gradebook.display_statistics()
            
            elif choice == 4:
                gradebook.create_sample_gradebook()
            
            elif choice == 5:
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 