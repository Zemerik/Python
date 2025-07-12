"""
Exercise 1: User Profile System
Create a user profile system that:
- Stores user info as dict (name, email, preferences)
- Allows updating preferences (add/remove items)
- Checks if mandatory fields exist
"""

class UserProfileSystem:
    def __init__(self):
        """Initialize the user profile system"""
        self.users = {}
        self.mandatory_fields = {'name', 'email'}
    
    def create_user(self, name, email, preferences=None):
        """Create a new user profile"""
        if not name or not email:
            print("Name and email are mandatory fields!")
            return False
        
        if email in self.users:
            print("User with this email already exists!")
            return False
        
        # Create user profile dictionary
        user_profile = {
            'name': name,
            'email': email,
            'preferences': preferences or set(),
            'created_date': '2024-01-15',  # Simulated date
            'last_updated': '2024-01-15'
        }
        
        self.users[email] = user_profile
        print(f"User profile created for {name}")
        return True
    
    def get_user(self, email):
        """Get user profile by email"""
        return self.users.get(email)
    
    def update_preferences(self, email, action, preference):
        """Update user preferences (add/remove items)"""
        user = self.get_user(email)
        if not user:
            print("User not found!")
            return False
        
        if action.lower() == 'add':
            user['preferences'].add(preference)
            print(f"Added '{preference}' to {user['name']}'s preferences")
        elif action.lower() == 'remove':
            if preference in user['preferences']:
                user['preferences'].remove(preference)
                print(f"Removed '{preference}' from {user['name']}'s preferences")
            else:
                print(f"'{preference}' not found in preferences")
        else:
            print("Invalid action. Use 'add' or 'remove'")
            return False
        
        user['last_updated'] = '2024-01-15'  # Simulated update
        return True
    
    def validate_user_profile(self, email):
        """Check if mandatory fields exist in user profile"""
        user = self.get_user(email)
        if not user:
            print("User not found!")
            return False
        
        missing_fields = self.mandatory_fields - set(user.keys())
        if missing_fields:
            print(f"Missing mandatory fields: {missing_fields}")
            return False
        
        # Check if mandatory fields have values
        for field in self.mandatory_fields:
            if not user[field]:
                print(f"Mandatory field '{field}' is empty")
                return False
        
        print("User profile is valid!")
        return True
    
    def display_user_profile(self, email):
        """Display complete user profile"""
        user = self.get_user(email)
        if not user:
            print("User not found!")
            return
        
        print(f"\n=== User Profile: {user['name']} ===")
        print(f"Email: {user['email']}")
        print(f"Preferences: {', '.join(user['preferences']) if user['preferences'] else 'None'}")
        print(f"Created: {user['created_date']}")
        print(f"Last Updated: {user['last_updated']}")
    
    def list_all_users(self):
        """List all users in the system"""
        if not self.users:
            print("No users in the system.")
            return
        
        print("\n=== All Users ===")
        for email, user in self.users.items():
            print(f"{user['name']} ({email})")
    
    def search_users_by_preference(self, preference):
        """Find users who have a specific preference"""
        matching_users = []
        for email, user in self.users.items():
            if preference in user['preferences']:
                matching_users.append(user['name'])
        
        if matching_users:
            print(f"Users with preference '{preference}': {', '.join(matching_users)}")
        else:
            print(f"No users found with preference '{preference}'")
        
        return matching_users

def get_user_input():
    """Get user information from input"""
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    
    preferences = set()
    print("Enter preferences (one per line, press Enter twice to finish):")
    while True:
        pref = input().strip()
        if not pref:
            break
        preferences.add(pref)
    
    return name, email, preferences

def display_menu():
    """Display the main menu"""
    print("\n=== User Profile System Menu ===")
    print("1. Create new user")
    print("2. View user profile")
    print("3. Update preferences")
    print("4. Validate user profile")
    print("5. List all users")
    print("6. Search users by preference")
    print("7. Exit")

def main():
    print("=== User Profile System ===")
    profile_system = UserProfileSystem()
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-7): "))
            
            if choice == 1:
                name, email, preferences = get_user_input()
                profile_system.create_user(name, email, preferences)
            
            elif choice == 2:
                email = input("Enter user email: ")
                profile_system.display_user_profile(email)
            
            elif choice == 3:
                email = input("Enter user email: ")
                action = input("Enter action (add/remove): ")
                preference = input("Enter preference: ")
                profile_system.update_preferences(email, action, preference)
            
            elif choice == 4:
                email = input("Enter user email: ")
                profile_system.validate_user_profile(email)
            
            elif choice == 5:
                profile_system.list_all_users()
            
            elif choice == 6:
                preference = input("Enter preference to search for: ")
                profile_system.search_users_by_preference(preference)
            
            elif choice == 7:
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 7.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 