"""
Exercise 1: Shopping Cart Program
Create a shopping cart program that:
- Allows adding/removing items
- Displays total items and unique items
- Calculates total price (items with prices)
"""

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = []  # List of (item_name, price) tuples
        self.prices = {
            'apple': 0.50,
            'banana': 0.30,
            'bread': 2.00,
            'milk': 1.50,
            'eggs': 3.00,
            'cheese': 4.50,
            'chicken': 8.00,
            'rice': 2.50,
            'tomato': 1.00,
            'potato': 0.80
        }
    
    def add_item(self, item_name, quantity=1):
        """Add items to the cart"""
        if item_name.lower() in self.prices:
            for _ in range(quantity):
                self.items.append((item_name.lower(), self.prices[item_name.lower()]))
            print(f"Added {quantity} {item_name}(s) to cart")
        else:
            print(f"Sorry, {item_name} is not available in our store.")
    
    def remove_item(self, item_name):
        """Remove the first occurrence of an item from the cart"""
        for i, (name, price) in enumerate(self.items):
            if name.lower() == item_name.lower():
                removed_item = self.items.pop(i)
                print(f"Removed {removed_item[0]} from cart")
                return
        print(f"{item_name} not found in cart")
    
    def display_cart(self):
        """Display current cart contents"""
        if not self.items:
            print("Your cart is empty!")
            return
        
        print("\n=== Shopping Cart ===")
        
        # Count items
        item_counts = {}
        for item_name, price in self.items:
            item_counts[item_name] = item_counts.get(item_name, 0) + 1
        
        # Display items with counts
        for item_name, count in item_counts.items():
            price = self.prices[item_name]
            total_price = price * count
            print(f"{item_name.title()}: {count} x ${price:.2f} = ${total_price:.2f}")
        
        # Display summary
        print("-" * 30)
        print(f"Total items: {len(self.items)}")
        print(f"Unique items: {len(item_counts)}")
        print(f"Total price: ${self.calculate_total():.2f}")
    
    def calculate_total(self):
        """Calculate total price of all items"""
        return sum(price for _, price in self.items)
    
    def clear_cart(self):
        """Clear all items from cart"""
        self.items.clear()
        print("Cart cleared!")

def display_menu():
    """Display the main menu"""
    print("\n=== Shopping Cart Menu ===")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Clear cart")
    print("5. Show available items")
    print("6. Exit")

def show_available_items(cart):
    """Show all available items and their prices"""
    print("\n=== Available Items ===")
    for item, price in cart.prices.items():
        print(f"{item.title()}: ${price:.2f}")

def get_user_choice():
    """Get user's menu choice"""
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Welcome to the Shopping Cart System ===")
    cart = ShoppingCart()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity (default 1): ") or "1")
                if quantity > 0:
                    cart.add_item(item_name, quantity)
                else:
                    print("Quantity must be positive.")
            except ValueError:
                cart.add_item(item_name, 1)
        
        elif choice == 2:
            item_name = input("Enter item name to remove: ")
            cart.remove_item(item_name)
        
        elif choice == 3:
            cart.display_cart()
        
        elif choice == 4:
            cart.clear_cart()
        
        elif choice == 5:
            show_available_items(cart)
        
        elif choice == 6:
            print("Thank you for shopping with us!")
            break

if __name__ == "__main__":
    main() 