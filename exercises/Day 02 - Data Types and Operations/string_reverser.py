"""
Exercise 2: String Reverser
Make a string reverser
"""


def reverse_string(text):
    """Reverse a string using string slicing"""
    return text[::-1]


def reverse_string_manual(text):
    """Reverse a string manually using a loop"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


def get_user_string():
    """Get string input from user"""
    return input("Enter a string to reverse: ")


def display_reversed_string(original, reversed_text):
    """Display the original and reversed string"""
    print(f"Original: {original}")
    print(f"Reversed: {reversed_text}")


def main():
    print("=== String Reverser ===")
    print()
    
    # Get input from user
    user_string = get_user_string()
    
    # Reverse using slicing method
    reversed_slice = reverse_string(user_string)
    print("\nMethod 1 - String Slicing:")
    display_reversed_string(user_string, reversed_slice)
    
    # Reverse using manual method
    reversed_manual = reverse_string_manual(user_string)
    print("\nMethod 2 - Manual Loop:")
    display_reversed_string(user_string, reversed_manual)
    
    # Verify both methods give same result
    if reversed_slice == reversed_manual:
        print("\n✓ Both methods produce the same result!")

if __name__ == "__main__":
    main() 