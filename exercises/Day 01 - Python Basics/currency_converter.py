"""
Exercise 2: Currency Converter
Make a currency converter from USD to EUR (hardcode rate)
"""


def convert_usd_to_eur(usd_amount):
    """Convert USD amount to EUR using hardcoded rate"""
    # Hardcoded exchange rate (1 USD = 0.85 EUR)
    exchange_rate = 0.85
    eur_amount = usd_amount * exchange_rate
    return eur_amount


def get_usd_amount():
    """Get USD amount from user input"""
    while True:
        try:
            amount = float(input("Enter amount in USD: $"))
            if amount < 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def display_conversion(usd_amount, eur_amount):
    """Display the conversion result"""
    print(f"${usd_amount:.2f} USD = \u20ac{eur_amount:.2f} EUR")


def main():
    print("=== USD to EUR Currency Converter ===")
    print("Exchange rate: 1 USD = 0.85 EUR")
    print()
    
    usd_amount = get_usd_amount()
    eur_amount = convert_usd_to_eur(usd_amount)
    display_conversion(usd_amount, eur_amount)

if __name__ == "__main__":
    main() 