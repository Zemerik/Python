"""
Exercise 1: Email Validator
Create an email validator that:
- Matches standard email formats
- Rejects invalid characters
- Extracts domain name
"""

import re

class EmailValidator:
    """Email validator using regular expressions"""
    
    EMAIL_PATTERN = re.compile(r"""
        ^([a-zA-Z0-9_.+-]+)      # username
        @                       # @ symbol
        ([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$ # domain
    """, re.VERBOSE)
    
    def validate(self, email):
        """Validate email and extract domain"""
        match = self.EMAIL_PATTERN.match(email)
        if not match:
            print(f"Invalid email: {email}")
            return False, None
        username, domain = match.groups()
        # Check for invalid characters
        if not re.match(r'^[a-zA-Z0-9_.+-]+$', username):
            print(f"Invalid characters in username: {username}")
            return False, None
        print(f"Valid email: {email} (domain: {domain})")
        return True, domain
    
    def extract_domain(self, email):
        """Extract domain from email if valid"""
        valid, domain = self.validate(email)
        return domain if valid else None

def main():
    print("=== Email Validator ===")
    validator = EmailValidator()
    emails = [
        "user@example.com",
        "john.doe@sub.domain.org",
        "invalid-email@.com",
        "bad!char@domain.com",
        "alice@company.co.uk",
        "bob@site",
        "user@domain-with-dash.com"
    ]
    for email in emails:
        validator.validate(email)

if __name__ == "__main__":
    main() 