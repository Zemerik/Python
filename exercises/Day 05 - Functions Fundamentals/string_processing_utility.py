"""
Exercise 2: String Processing Utility
Build a string processing utility with functions that:
- Count vowels in a string
- Reverse the string
- Check if palindrome
- Returns statistics in dictionary format
"""


def count_vowels(text):
    """Count the number of vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def reverse_string(text):
    """Reverse a string"""
    return text[::-1]


def is_palindrome(text):
    """Check if a string is a palindrome (ignoring case and spaces)"""
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def get_string_statistics(text):
    """Get comprehensive statistics about a string"""
    stats = {
        'original': text,
        'length': len(text),
        'vowel_count': count_vowels(text),
        'consonant_count': sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou'),
        'digit_count': sum(1 for char in text if char.isdigit()),
        'space_count': text.count(' '),
        'uppercase_count': sum(1 for char in text if char.isupper()),
        'lowercase_count': sum(1 for char in text if char.islower()),
        'reversed': reverse_string(text),
        'is_palindrome': is_palindrome(text),
        'word_count': len(text.split()) if text.strip() else 0
    }
    return stats


def display_statistics(stats):
    """Display string statistics in a formatted way"""
    print("\n=== String Statistics ===")
    print(f"Original text: '{stats['original']}'")
    print(f"Length: {stats['length']} characters")
    print(f"Words: {stats['word_count']}")
    print(f"Vowels: {stats['vowel_count']}")
    print(f"Consonants: {stats['consonant_count']}")
    print(f"Digits: {stats['digit_count']}")
    print(f"Spaces: {stats['space_count']}")
    print(f"Uppercase letters: {stats['uppercase_count']}")
    print(f"Lowercase letters: {stats['lowercase_count']}")
    print(f"Reversed: '{stats['reversed']}'")
    print(f"Is palindrome: {'Yes' if stats['is_palindrome'] else 'No'}")


def get_user_string():
    """Get string input from user"""
    return input("Enter a string to analyze: ")


def main():
    print("=== String Processing Utility ===")
    
    while True:
        # Get input from user
        user_text = get_user_string()
        
        if not user_text.strip():
            print("Please enter a non-empty string.")
            continue
        
        # Get statistics
        stats = get_string_statistics(user_text)
        
        # Display results
        display_statistics(stats)
        
        # Show individual function results
        print(f"\n=== Individual Function Results ===")
        print(f"Vowel count: {count_vowels(user_text)}")
        print(f"Reversed string: '{reverse_string(user_text)}'")
        print(f"Is palindrome: {'Yes' if is_palindrome(user_text) else 'No'}")
        
        # Ask if user wants to process another string
        another = input("\nProcess another string? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 