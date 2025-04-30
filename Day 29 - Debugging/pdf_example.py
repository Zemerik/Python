import pdb

def calculate_discount(price, discount):
    pdb.set_trace()  # Breakpoint
    if discount > 0.5:
        print("Warning: Large discount applied")
    return price - (price * discount)

# Debug this calculation
print(calculate_discount(100, 0.6))