"""
Exercise 2: Shipping Cost Calculator
Make a shipping cost calculator with:
- Weight tiers (under 1kg, 1-5kg, over 5kg)
- Regional surcharges
"""


def calculate_weight_cost(weight_kg):
    """Calculate base shipping cost based on weight tiers"""
    if weight_kg < 1:
        return 5.00  # Under 1kg
    elif 1 <= weight_kg <= 5:
        return 10.00  # 1-5kg
    else:
        return 15.00  # Over 5kg


def get_regional_surcharge(region):
    """Get regional surcharge based on destination"""
    surcharges = {
        "local": 0.00,      # No surcharge
        "domestic": 2.50,   # Domestic shipping
        "international": 15.00,  # International shipping
        "remote": 8.00      # Remote areas
    }
    return surcharges.get(region.lower(), 0.00)


def get_user_input():
    """Get package details from user"""
    while True:
        try:
            weight = float(input("Enter package weight in kg: "))
            if weight <= 0:
                print("Weight must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for weight.")
    
    print("\nAvailable regions:")
    print("1. Local")
    print("2. Domestic")
    print("3. International")
    print("4. Remote")
    
    while True:
        region_choice = input("Select region (1-4): ")
        region_map = {
            "1": "local",
            "2": "domestic", 
            "3": "international",
            "4": "remote"
        }
        if region_choice in region_map:
            region = region_map[region_choice]
            break
        else:
            print("Please select a valid option (1-4).")
    
    return weight, region


def calculate_total_cost(weight, region):
    """Calculate total shipping cost"""
    base_cost = calculate_weight_cost(weight)
    surcharge = get_regional_surcharge(region)
    total = base_cost + surcharge
    return base_cost, surcharge, total


def display_cost_breakdown(weight, region, base_cost, surcharge, total):
    """Display detailed cost breakdown"""
    print(f"\n=== Shipping Cost Breakdown ===")
    print(f"Package weight: {weight} kg")
    print(f"Destination: {region.title()}")
    print(f"Base cost: ${base_cost:.2f}")
    print(f"Regional surcharge: ${surcharge:.2f}")
    print(f"Total shipping cost: ${total:.2f}")


def main():
    print("=== Shipping Cost Calculator ===")
    print()
    
    # Get package details
    weight, region = get_user_input()
    
    # Calculate costs
    base_cost, surcharge, total = calculate_total_cost(weight, region)
    
    # Display results
    display_cost_breakdown(weight, region, base_cost, surcharge, total)

if __name__ == "__main__":
    main() 