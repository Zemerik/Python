"""
Exercise 2: Student Grade System
Build a student grade system using tuples that:
- Stores student records as (name, math_score, science_score)
- Unpacks tuples to calculate average scores
- Finds top performer in each subject
"""

class StudentGradeSystem:
    def __init__(self):
        """Initialize the grade system with sample student data"""
        # Student records as tuples: (name, math_score, science_score)
        self.students = [
            ("Alice Johnson", 85, 92),
            ("Bob Smith", 78, 88),
            ("Charlie Brown", 92, 85),
            ("Diana Prince", 95, 90),
            ("Eve Wilson", 88, 87),
            ("Frank Miller", 76, 82),
            ("Grace Lee", 91, 94),
            ("Henry Davis", 83, 79),
            ("Ivy Chen", 89, 91),
            ("Jack Taylor", 94, 88)
        ]
    
    def add_student(self, name, math_score, science_score):
        """Add a new student record"""
        if 0 <= math_score <= 100 and 0 <= science_score <= 100:
            self.students.append((name, math_score, science_score))
            print(f"Added student: {name}")
        else:
            print("Scores must be between 0 and 100")
    
    def calculate_average_scores(self):
        """Calculate average scores for each student"""
        averages = []
        for student in self.students:
            name, math, science = student  # Tuple unpacking
            average = (math + science) / 2
            averages.append((name, average))
        return averages
    
    def find_top_performer(self, subject_index):
        """Find the top performer in a specific subject"""
        if not self.students:
            return None
        
        # subject_index: 1 for math, 2 for science
        top_student = max(self.students, key=lambda x: x[subject_index])
        return top_student
    
    def get_subject_averages(self):
        """Calculate class averages for each subject"""
        if not self.students:
            return 0, 0
        
        math_scores = [student[1] for student in self.students]
        science_scores = [student[2] for student in self.students]
        
        math_average = sum(math_scores) / len(math_scores)
        science_average = sum(science_scores) / len(science_scores)
        
        return math_average, science_average
    
    def display_all_students(self):
        """Display all student records with averages"""
        print("\n=== Student Grade Report ===")
        print(f"{'Name':<20} {'Math':<8} {'Science':<8} {'Average':<8}")
        print("-" * 50)
        
        averages = self.calculate_average_scores()
        for i, student in enumerate(self.students):
            name, math, science = student
            average = averages[i][1]
            print(f"{name:<20} {math:<8} {science:<8} {average:<8.1f}")
    
    def display_top_performers(self):
        """Display top performers in each subject"""
        print("\n=== Top Performers ===")
        
        # Top in Math
        top_math = self.find_top_performer(1)
        if top_math:
            name, math, science = top_math
            print(f"Top Math Student: {name} (Score: {math})")
        
        # Top in Science
        top_science = self.find_top_performer(2)
        if top_science:
            name, math, science = top_science
            print(f"Top Science Student: {name} (Score: {science})")
    
    def display_class_statistics(self):
        """Display class-wide statistics"""
        print("\n=== Class Statistics ===")
        
        math_avg, science_avg = self.get_subject_averages()
        print(f"Class Math Average: {math_avg:.1f}")
        print(f"Class Science Average: {science_avg:.1f}")
        print(f"Total Students: {len(self.students)}")
        
        # Find students above average in both subjects
        above_average = []
        for student in self.students:
            name, math, science = student
            if math > math_avg and science > science_avg:
                above_average.append(name)
        
        if above_average:
            print(f"Students above average in both subjects: {', '.join(above_average)}")
        else:
            print("No students above average in both subjects")

def get_student_input():
    """Get new student information from user"""
    name = input("Enter student name: ")
    
    while True:
        try:
            math_score = int(input("Enter math score (0-100): "))
            if 0 <= math_score <= 100:
                break
            else:
                print("Math score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            science_score = int(input("Enter science score (0-100): "))
            if 0 <= science_score <= 100:
                break
            else:
                print("Science score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    return name, math_score, science_score

def display_menu():
    """Display the main menu"""
    print("\n=== Student Grade System Menu ===")
    print("1. View all students")
    print("2. Add new student")
    print("3. View top performers")
    print("4. View class statistics")
    print("5. Exit")

def main():
    print("=== Student Grade System ===")
    grade_system = StudentGradeSystem()
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                grade_system.display_all_students()
            
            elif choice == 2:
                name, math, science = get_student_input()
                grade_system.add_student(name, math, science)
            
            elif choice == 3:
                grade_system.display_top_performers()
            
            elif choice == 4:
                grade_system.display_class_statistics()
            
            elif choice == 5:
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 