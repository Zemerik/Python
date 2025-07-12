"""
Exercise 1: Login System
Create a login system that checks both username and password
"""


def validate_credentials(username, password):
    """Validate username and password against stored credentials"""
    # In a real application, these would be stored securely in a database
    # For this exercise, we'll use hardcoded credentials
    valid_credentials = {
        "admin": "password123",
        "user1": "secret456",
        "john": "mypass789"
    }
    
    if username in valid_credentials:
        if valid_credentials[username] == password:
            return True, "Login successful!"
        else:
            return False, "Incorrect password."
    else:
        return False, "Username not found."


def get_user_input():
    """Get username and password from user"""
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password


def display_login_result(success, message):
    """Display login result to user"""
    if success:
        print(f"\u2713 {message}")
        print("Welcome to the system!")
    else:
        print(f"\u2717 {message}")
        print("Please try again.")


def main():
    print("=== Login System ===")
    print("Available accounts for testing:")
    print("- admin / password123")
    print("- user1 / secret456")
    print("- john / mypass789")
    print()
    
    # Get user credentials
    username, password = get_user_input()
    
    # Validate credentials
    success, message = validate_credentials(username, password)
    
    # Display result
    display_login_result(success, message)

if __name__ == "__main__":
    main() 