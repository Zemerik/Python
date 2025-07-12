"""
Exercise 1: Name and Age Program
Create a program that asks for your name and age, then prints them
"""


def get_user_info():
    """Get user's name and age from input"""
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    return name, age


def display_user_info(name, age):
    """Display the user's information"""
    print(f"Hello {name}!")
    print(f"You are {age} years old.")


def main():
    print("=== Name and Age Program ===")
    name, age = get_user_info()
    display_user_info(name, age)

if __name__ == "__main__":
    main() 