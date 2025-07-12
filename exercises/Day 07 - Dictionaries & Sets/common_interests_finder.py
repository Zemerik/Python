"""
Exercise 2: Common Interests Finder
Build a common interests finder that:
- Takes 2 sets of hobbies/interests
- Identifies shared interests
- Shows unique interests per person
"""

class CommonInterestsFinder:
    def __init__(self):
        """Initialize the interests finder"""
        self.people = {}
    
    def add_person(self, name, interests):
        """Add a person with their interests"""
        if not name or not interests:
            print("Name and interests are required!")
            return False
        
        # Convert interests to a set to ensure uniqueness
        interests_set = set(interest.strip().lower() for interest in interests)
        self.people[name] = interests_set
        print(f"Added {name} with {len(interests_set)} interests")
        return True
    
    def find_common_interests(self, person1, person2):
        """Find common interests between two people"""
        if person1 not in self.people or person2 not in self.people:
            print("One or both people not found!")
            return set()
        
        interests1 = self.people[person1]
        interests2 = self.people[person2]
        
        # Use set intersection to find common interests
        common = interests1 & interests2
        return common
    
    def find_unique_interests(self, person1, person2):
        """Find unique interests for each person"""
        if person1 not in self.people or person2 not in self.people:
            print("One or both people not found!")
            return {}, {}
        
        interests1 = self.people[person1]
        interests2 = self.people[person2]
        
        # Use set difference to find unique interests
        unique_to_person1 = interests1 - interests2
        unique_to_person2 = interests2 - interests1
        
        return unique_to_person1, unique_to_person2
    
    def find_all_common_interests(self):
        """Find interests that are common among all people"""
        if len(self.people) < 2:
            print("Need at least 2 people to find common interests!")
            return set()
        
        # Start with the first person's interests
        all_common = set(self.people[list(self.people.keys())[0]])
        
        # Intersect with each person's interests
        for interests in self.people.values():
            all_common &= interests
        
        return all_common
    
    def find_interest_compatibility(self, person1, person2):
        """Calculate compatibility score based on shared interests"""
        if person1 not in self.people or person2 not in self.people:
            return 0
        
        interests1 = self.people[person1]
        interests2 = self.people[person2]
        
        if not interests1 and not interests2:
            return 100  # Both have no interests, perfect match? 😄
        
        # Calculate Jaccard similarity
        intersection = len(interests1 & interests2)
        union = len(interests1 | interests2)
        
        if union == 0:
            return 0
        
        compatibility = (intersection / union) * 100
        return round(compatibility, 1)
    
    def display_comparison(self, person1, person2):
        """Display detailed comparison between two people"""
        if person1 not in self.people or person2 not in self.people:
            print("One or both people not found!")
            return
        
        print(f"\n=== Interest Comparison: {person1} vs {person2} ===")
        
        # Get all the data
        common = self.find_common_interests(person1, person2)
        unique1, unique2 = self.find_unique_interests(person1, person2)
        compatibility = self.find_interest_compatibility(person1, person2)
        
        # Display results
        print(f"\n{person1}'s interests: {', '.join(self.people[person1])}")
        print(f"{person2}'s interests: {', '.join(self.people[person2])}")
        
        print(f"\nCommon interests ({len(common)}): {', '.join(common) if common else 'None'}")
        print(f"{person1}'s unique interests ({len(unique1)}): {', '.join(unique1) if unique1 else 'None'}")
        print(f"{person2}'s unique interests ({len(unique2)}): {', '.join(unique2) if unique2 else 'None'}")
        
        print(f"\nCompatibility score: {compatibility}%")
        
        # Give a fun interpretation
        if compatibility >= 80:
            print("🎉 Excellent compatibility! You two would get along great!")
        elif compatibility >= 60:
            print("😊 Good compatibility! You have some nice shared interests.")
        elif compatibility >= 40:
            print("🤔 Moderate compatibility. You might find some common ground.")
        elif compatibility >= 20:
            print("😐 Low compatibility. You're quite different!")
        else:
            print("😅 Very low compatibility. Opposites attract?")
    
    def list_all_people(self):
        """List all people and their interest counts"""
        if not self.people:
            print("No people added yet.")
            return
        
        print("\n=== All People ===")
        for name, interests in self.people.items():
            print(f"{name}: {len(interests)} interests")

def get_interests_input():
    """Get interests from user input"""
    print("Enter interests (one per line, press Enter twice to finish):")
    interests = []
    while True:
        interest = input().strip()
        if not interest:
            break
        interests.append(interest)
    return interests

def display_menu():
    """Display the main menu"""
    print("\n=== Common Interests Finder Menu ===")
    print("1. Add person")
    print("2. Compare two people")
    print("3. Find all common interests")
    print("4. List all people")
    print("5. Exit")

def main():
    print("=== Common Interests Finder ===")
    finder = CommonInterestsFinder()
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                name = input("Enter person's name: ").strip()
                interests = get_interests_input()
                finder.add_person(name, interests)
            
            elif choice == 2:
                if len(finder.people) < 2:
                    print("Need at least 2 people to compare!")
                    continue
                
                finder.list_all_people()
                person1 = input("Enter first person's name: ").strip()
                person2 = input("Enter second person's name: ").strip()
                finder.display_comparison(person1, person2)
            
            elif choice == 3:
                common = finder.find_all_common_interests()
                if common:
                    print(f"\nInterests common to all people: {', '.join(common)}")
                else:
                    print("\nNo interests common to all people.")
            
            elif choice == 4:
                finder.list_all_people()
            
            elif choice == 5:
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 