"""
Exercise 2: Payment Processor System
Build a payment processor system with:
- Base PaymentMethod class
- CreditCard, PayPal, and Crypto subclasses
- Common process_payment() interface
"""

from abc import ABC, abstractmethod
import random
from datetime import datetime

class PaymentMethod(ABC):
    """Abstract base class for payment methods"""
    
    def __init__(self, name):
        """Initialize payment method with name"""
        self.name = name
        self.transaction_history = []
    
    @abstractmethod
    def process_payment(self, amount, description=""):
        """
        Process a payment
        
        Args:
            amount (float): Payment amount
            description (str): Payment description
        
        Returns:
            dict: Payment result with status and details
        """
        pass
    
    @abstractmethod
    def validate_payment(self, amount):
        """
        Validate if payment can be processed
        
        Args:
            amount (float): Payment amount
        
        Returns:
            bool: True if valid, False otherwise
        """
        pass
    
    def record_transaction(self, amount, description, status, details=""):
        """Record a transaction in history"""
        transaction = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'description': description,
            'status': status,
            'details': details
        }
        self.transaction_history.append(transaction)
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self.transaction_history
    
    def display_info(self):
        """Display payment method information"""
        print(f"\n=== {self.name} Payment Method ===")
        print(f"Total Transactions: {len(self.transaction_history)}")

class CreditCard(PaymentMethod):
    """Credit card payment method"""
    
    def __init__(self, card_number, expiry_date, cvv, cardholder_name):
        """Initialize credit card"""
        super().__init__("Credit Card")
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.cardholder_name = cardholder_name
        self.credit_limit = 10000.0
        self.current_balance = 0.0
    
    def validate_payment(self, amount):
        """Validate credit card payment"""
        if amount <= 0:
            return False, "Invalid amount"
        
        if amount > (self.credit_limit - self.current_balance):
            return False, "Insufficient credit limit"
        
        # Simulate card validation
        if not self._is_valid_card():
            return False, "Invalid card details"
        
        return True, "Valid"
    
    def _is_valid_card(self):
        """Validate card details (simplified)"""
        # Basic validation - in real world, this would be more complex
        return (len(self.card_number) == 16 and 
                len(self.cvv) == 3 and 
                self.cardholder_name.strip())
    
    def process_payment(self, amount, description=""):
        """Process credit card payment"""
        is_valid, message = self.validate_payment(amount)
        
        if not is_valid:
            self.record_transaction(amount, description, "Failed", message)
            return {
                'success': False,
                'message': message,
                'transaction_id': None
            }
        
        # Simulate payment processing
        transaction_id = f"CC{random.randint(100000, 999999)}"
        
        # Simulate processing delay and potential failure
        if random.random() < 0.05:  # 5% failure rate
            self.record_transaction(amount, description, "Failed", "Processing error")
            return {
                'success': False,
                'message': "Payment processing failed",
                'transaction_id': None
            }
        
        # Successful payment
        self.current_balance += amount
        self.record_transaction(amount, description, "Success", f"Transaction ID: {transaction_id}")
        
        return {
            'success': True,
            'message': "Payment processed successfully",
            'transaction_id': transaction_id,
            'amount': amount
        }
    
    def display_info(self):
        """Display credit card information"""
        super().display_info()
        print(f"Cardholder: {self.cardholder_name}")
        print(f"Card Number: **** **** **** {self.card_number[-4:]}")
        print(f"Expiry Date: {self.expiry_date}")
        print(f"Credit Limit: ${self.credit_limit:.2f}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Available Credit: ${self.credit_limit - self.current_balance:.2f}")

class PayPal(PaymentMethod):
    """PayPal payment method"""
    
    def __init__(self, email, password):
        """Initialize PayPal account"""
        super().__init__("PayPal")
        self.email = email
        self.password = password
        self.balance = 5000.0  # Simulated balance
        self.is_verified = True
    
    def validate_payment(self, amount):
        """Validate PayPal payment"""
        if amount <= 0:
            return False, "Invalid amount"
        
        if amount > self.balance:
            return False, "Insufficient PayPal balance"
        
        if not self.is_verified:
            return False, "PayPal account not verified"
        
        return True, "Valid"
    
    def process_payment(self, amount, description=""):
        """Process PayPal payment"""
        is_valid, message = self.validate_payment(amount)
        
        if not is_valid:
            self.record_transaction(amount, description, "Failed", message)
            return {
                'success': False,
                'message': message,
                'transaction_id': None
            }
        
        # Simulate payment processing
        transaction_id = f"PP{random.randint(100000, 999999)}"
        
        # Simulate processing delay and potential failure
        if random.random() < 0.03:  # 3% failure rate
            self.record_transaction(amount, description, "Failed", "PayPal processing error")
            return {
                'success': False,
                'message': "PayPal payment processing failed",
                'transaction_id': None
            }
        
        # Successful payment
        self.balance -= amount
        self.record_transaction(amount, description, "Success", f"Transaction ID: {transaction_id}")
        
        return {
            'success': True,
            'message': "PayPal payment processed successfully",
            'transaction_id': transaction_id,
            'amount': amount
        }
    
    def display_info(self):
        """Display PayPal information"""
        super().display_info()
        print(f"Email: {self.email}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Verified: {'Yes' if self.is_verified else 'No'}")

class Crypto(PaymentMethod):
    """Cryptocurrency payment method"""
    
    def __init__(self, wallet_address, crypto_type="Bitcoin"):
        """Initialize crypto wallet"""
        super().__init__("Cryptocurrency")
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
        self.balance = 2.5  # BTC balance
        self.exchange_rate = 45000.0  # USD per BTC
    
    def validate_payment(self, amount):
        """Validate crypto payment"""
        if amount <= 0:
            return False, "Invalid amount"
        
        # Convert USD to crypto amount
        crypto_amount = amount / self.exchange_rate
        
        if crypto_amount > self.balance:
            return False, f"Insufficient {self.crypto_type} balance"
        
        return True, "Valid"
    
    def process_payment(self, amount, description=""):
        """Process cryptocurrency payment"""
        is_valid, message = self.validate_payment(amount)
        
        if not is_valid:
            self.record_transaction(amount, description, "Failed", message)
            return {
                'success': False,
                'message': message,
                'transaction_id': None
            }
        
        # Simulate blockchain transaction
        transaction_id = f"CR{random.randint(100000, 999999)}"
        
        # Simulate blockchain processing (higher failure rate due to network issues)
        if random.random() < 0.08:  # 8% failure rate
            self.record_transaction(amount, description, "Failed", "Blockchain transaction failed")
            return {
                'success': False,
                'message': "Cryptocurrency transaction failed",
                'transaction_id': None
            }
        
        # Successful payment
        crypto_amount = amount / self.exchange_rate
        self.balance -= crypto_amount
        self.record_transaction(amount, description, "Success", f"Transaction ID: {transaction_id}")
        
        return {
            'success': True,
            'message': f"{self.crypto_type} payment processed successfully",
            'transaction_id': transaction_id,
            'amount': amount,
            'crypto_amount': crypto_amount
        }
    
    def display_info(self):
        """Display crypto information"""
        super().display_info()
        print(f"Crypto Type: {self.crypto_type}")
        print(f"Wallet Address: {self.wallet_address[:10]}...{self.wallet_address[-10:]}")
        print(f"Balance: {self.balance} {self.crypto_type}")
        print(f"Exchange Rate: ${self.exchange_rate:.2f} per {self.crypto_type}")
        print(f"USD Value: ${self.balance * self.exchange_rate:.2f}")

class PaymentProcessor:
    """Main payment processor system"""
    
    def __init__(self):
        """Initialize payment processor"""
        self.payment_methods = {}
        self.total_transactions = 0
        self.successful_transactions = 0
    
    def add_payment_method(self, method_id, payment_method):
        """Add a payment method to the processor"""
        self.payment_methods[method_id] = payment_method
        print(f"Added {payment_method.name} payment method")
    
    def process_payment(self, method_id, amount, description=""):
        """Process payment using specified method"""
        if method_id not in self.payment_methods:
            return {
                'success': False,
                'message': "Payment method not found",
                'transaction_id': None
            }
        
        payment_method = self.payment_methods[method_id]
        result = payment_method.process_payment(amount, description)
        
        self.total_transactions += 1
        if result['success']:
            self.successful_transactions += 1
        
        return result
    
    def list_payment_methods(self):
        """List all available payment methods"""
        if not self.payment_methods:
            print("No payment methods available.")
            return
        
        print(f"\n=== Available Payment Methods ({len(self.payment_methods)}) ===")
        for method_id, method in self.payment_methods.items():
            print(f"{method_id}: {method.name}")
    
    def get_payment_method_info(self, method_id):
        """Get information about a specific payment method"""
        if method_id not in self.payment_methods:
            print("Payment method not found.")
            return
        
        self.payment_methods[method_id].display_info()
    
    def display_statistics(self):
        """Display payment processing statistics"""
        success_rate = (self.successful_transactions / self.total_transactions * 100) if self.total_transactions > 0 else 0
        
        print(f"\n=== Payment Processor Statistics ===")
        print(f"Total Transactions: {self.total_transactions}")
        print(f"Successful Transactions: {self.successful_transactions}")
        print(f"Failed Transactions: {self.total_transactions - self.successful_transactions}")
        print(f"Success Rate: {success_rate:.1f}%")
        print(f"Payment Methods: {len(self.payment_methods)}")

def main():
    """Main function to demonstrate the payment processor system"""
    print("=== Payment Processor System ===")
    processor = PaymentProcessor()
    
    # Create sample payment methods
    credit_card = CreditCard("1234567890123456", "12/25", "123", "John Doe")
    paypal = PayPal("john.doe@example.com", "password123")
    crypto = Crypto("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "Bitcoin")
    
    processor.add_payment_method("CC", credit_card)
    processor.add_payment_method("PP", paypal)
    processor.add_payment_method("CR", crypto)
    
    while True:
        print("\nChoose an option:")
        print("1. List payment methods")
        print("2. View payment method details")
        print("3. Process payment")
        print("4. View transaction history")
        print("5. View statistics")
        print("6. Exit")
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                processor.list_payment_methods()
            
            elif choice == '2':
                processor.list_payment_methods()
                method_id = input("Enter payment method ID: ").strip()
                processor.get_payment_method_info(method_id)
            
            elif choice == '3':
                processor.list_payment_methods()
                method_id = input("Enter payment method ID: ").strip()
                
                try:
                    amount = float(input("Enter payment amount: $"))
                    description = input("Enter payment description (optional): ").strip()
                    
                    result = processor.process_payment(method_id, amount, description)
                    
                    if result['success']:
                        print(f"✅ {result['message']}")
                        print(f"Transaction ID: {result['transaction_id']}")
                    else:
                        print(f"❌ {result['message']}")
                
                except ValueError:
                    print("Please enter a valid amount.")
            
            elif choice == '4':
                processor.list_payment_methods()
                method_id = input("Enter payment method ID: ").strip()
                
                if method_id in processor.payment_methods:
                    method = processor.payment_methods[method_id]
                    history = method.get_transaction_history()
                    
                    if history:
                        print(f"\n=== Transaction History for {method.name} ===")
                        for transaction in history:
                            status_icon = "✅" if transaction['status'] == "Success" else "❌"
                            print(f"{status_icon} {transaction['timestamp']} - ${transaction['amount']:.2f} - {transaction['status']}")
                            if transaction['details']:
                                print(f"   Details: {transaction['details']}")
                    else:
                        print("No transactions found.")
                else:
                    print("Payment method not found.")
            
            elif choice == '5':
                processor.display_statistics()
            
            elif choice == '6':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 6.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 