import re

# Simple substitution
text = "Order: 12345, Status: pending"
redacted = re.sub(r"\d{5}", "XXXXX", text)
print("Redacted:", redacted)

# Replacement function
def stars(match):
    return '*' * len(match.group())

sensitive = "Card: 4111-1111-1111-1111"
secured = re.sub(r"\d{4}(-\d{4}){3}", stars, sensitive)
print("Secured:", secured)