"""
Exercise 1: BMI Calculator
Create a BMI calculator (weight/height²)
"""


def calculate_bmi(weight_kg, height_m):
    """Calculate BMI using the formula: weight / height²"""
    bmi = weight_kg / (height_m ** 2)
    return bmi


def get_bmi_category(bmi):
    """Determine BMI category based on calculated BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_user_measurements():
    """Get weight and height from user input"""
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                print("Weight must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for weight.")
    
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for height.")
    
    return weight, height


def display_bmi_result(bmi, category):
    """Display BMI calculation result"""
    print(f"\nYour BMI: {bmi:.1f}")
    print(f"Category: {category}")


def main():
    print("=== BMI Calculator ===")
    print("Formula: BMI = weight (kg) / height (m)²")
    print()
    
    weight, height = get_user_measurements()
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    display_bmi_result(bmi, category)

if __name__ == "__main__":
    main() 