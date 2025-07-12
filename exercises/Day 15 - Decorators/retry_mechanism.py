"""
Exercise 2: Retry Mechanism Decorator
Build a retry mechanism decorator that:
- Retries failed operations (3 attempts)
- Implements exponential backoff
- Logs retry attempts
"""

import time
import functools
import logging
import random
from datetime import datetime
import os

class RetryMechanism:
    """Retry mechanism decorator with exponential backoff and logging"""
    
    def __init__(self, max_attempts=3, base_delay=1, max_delay=60, backoff_factor=2, 
                 exceptions=(Exception,), log_file="retry_attempts.log"):
        """
        Initialize retry mechanism
        
        Args:
            max_attempts (int): Maximum number of retry attempts
            base_delay (float): Base delay in seconds
            max_delay (float): Maximum delay in seconds
            backoff_factor (float): Exponential backoff factor
            exceptions (tuple): Exceptions to catch and retry
            log_file (str): Log file path
        """
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.exceptions = exceptions
        self.log_file = log_file
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def __call__(self, func):
        """Main decorator method"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            last_exception = None
            
            for attempt in range(1, self.max_attempts + 1):
                try:
                    # Log attempt
                    logging.info(f"Function '{func_name}' - Attempt {attempt}/{self.max_attempts}")
                    
                    # Execute function
                    result = func(*args, **kwargs)
                    
                    # Log success
                    logging.info(f"Function '{func_name}' - Attempt {attempt} succeeded")
                    return result
                    
                except self.exceptions as e:
                    last_exception = e
                    
                    # Log failure
                    logging.warning(f"Function '{func_name}' - Attempt {attempt} failed: {str(e)}")
                    
                    # If this is the last attempt, don't wait
                    if attempt == self.max_attempts:
                        logging.error(f"Function '{func_name}' - All {self.max_attempts} attempts failed")
                        break
                    
                    # Calculate delay with exponential backoff
                    delay = min(self.base_delay * (self.backoff_factor ** (attempt - 1)), self.max_delay)
                    
                    # Add jitter to prevent thundering herd
                    jitter = random.uniform(0, 0.1 * delay)
                    total_delay = delay + jitter
                    
                    # Log retry delay
                    logging.info(f"Function '{func_name}' - Waiting {total_delay:.2f} seconds before retry")
                    
                    # Wait before retry
                    time.sleep(total_delay)
            
            # If we get here, all attempts failed
            logging.error(f"Function '{func_name}' - Final failure after {self.max_attempts} attempts")
            raise last_exception
        
        return wrapper

def retry_mechanism(max_attempts=3, base_delay=1, max_delay=60, backoff_factor=2, 
                   exceptions=(Exception,), log_file="retry_attempts.log"):
    """Alternative decorator function approach"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Setup logging for this call
            logging.basicConfig(
                filename=log_file,
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            func_name = func.__name__
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    # Log attempt
                    logging.info(f"Function '{func_name}' - Attempt {attempt}/{max_attempts}")
                    
                    # Execute function
                    result = func(*args, **kwargs)
                    
                    # Log success
                    logging.info(f"Function '{func_name}' - Attempt {attempt} succeeded")
                    return result
                    
                except exceptions as e:
                    last_exception = e
                    
                    # Log failure
                    logging.warning(f"Function '{func_name}' - Attempt {attempt} failed: {str(e)}")
                    
                    # If this is the last attempt, don't wait
                    if attempt == max_attempts:
                        logging.error(f"Function '{func_name}' - All {max_attempts} attempts failed")
                        break
                    
                    # Calculate delay with exponential backoff
                    delay = min(base_delay * (backoff_factor ** (attempt - 1)), max_delay)
                    
                    # Add jitter to prevent thundering herd
                    jitter = random.uniform(0, 0.1 * delay)
                    total_delay = delay + jitter
                    
                    # Log retry delay
                    logging.info(f"Function '{func_name}' - Waiting {total_delay:.2f} seconds before retry")
                    
                    # Wait before retry
                    time.sleep(total_delay)
            
            # If we get here, all attempts failed
            logging.error(f"Function '{func_name}' - Final failure after {max_attempts} attempts")
            raise last_exception
        
        return wrapper
    return decorator

# Example functions to demonstrate the retry mechanism
@RetryMechanism(max_attempts=3, base_delay=0.5, exceptions=(ValueError,))
def unreliable_division(a, b):
    """Simulate an unreliable division operation"""
    # Simulate random failures
    if random.random() < 0.7:  # 70% failure rate
        raise ValueError("Simulated division error")
    return a / b

@RetryMechanism(max_attempts=5, base_delay=0.2, backoff_factor=1.5, exceptions=(ConnectionError,))
def simulate_network_request(url):
    """Simulate a network request that might fail"""
    # Simulate network failures
    if random.random() < 0.6:  # 60% failure rate
        raise ConnectionError(f"Failed to connect to {url}")
    
    # Simulate processing time
    time.sleep(0.1)
    return f"Successfully retrieved data from {url}"

@retry_mechanism(max_attempts=4, base_delay=0.3, exceptions=(FileNotFoundError,))
def read_file_with_retry(filename):
    """Simulate reading a file that might not exist initially"""
    # Simulate file system delays
    if random.random() < 0.5:  # 50% failure rate
        raise FileNotFoundError(f"File {filename} not found")
    
    # Simulate file reading
    time.sleep(0.05)
    return f"Content of {filename}"

class DatabaseOperations:
    """Class with retry mechanism for database operations"""
    
    def __init__(self):
        self.retry_decorator = RetryMechanism(
            max_attempts=3, 
            base_delay=1, 
            exceptions=(ConnectionError, TimeoutError),
            log_file="database_operations.log"
        )
    
    @property
    def decorated_query(self):
        """Property to get decorated query method"""
        return self.retry_decorator(self._query)
    
    def _query(self, query_string):
        """Internal method to be decorated"""
        # Simulate database query failures
        if random.random() < 0.4:  # 40% failure rate
            raise ConnectionError("Database connection lost")
        
        time.sleep(0.1)
        return f"Query result: {query_string}"

def demonstrate_retry_mechanism():
    """Demonstrate the retry mechanism decorator"""
    print("=== Retry Mechanism Decorator Demonstration ===")
    
    # Test unreliable division
    print("\n1. Testing unreliable division:")
    try:
        result = unreliable_division(10, 2)
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")
    
    # Test network request
    print("\n2. Testing network request:")
    try:
        result = simulate_network_request("https://api.example.com")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")
    
    # Test file reading
    print("\n3. Testing file reading:")
    try:
        result = read_file_with_retry("example.txt")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")
    
    # Test database operations
    print("\n4. Testing database operations:")
    db_ops = DatabaseOperations()
    try:
        result = db_ops.decorated_query("SELECT * FROM users")
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")

def demonstrate_different_configurations():
    """Demonstrate different retry configurations"""
    print("\n=== Different Retry Configurations ===")
    
    # Fast retry with short delays
    @RetryMechanism(max_attempts=3, base_delay=0.1, backoff_factor=1.5, 
                   exceptions=(ValueError,), log_file="fast_retry.log")
    def fast_operation():
        if random.random() < 0.8:  # 80% failure rate
            raise ValueError("Fast operation failed")
        return "Fast operation succeeded"
    
    # Slow retry with long delays
    @RetryMechanism(max_attempts=2, base_delay=2, backoff_factor=3, 
                   exceptions=(ValueError,), log_file="slow_retry.log")
    def slow_operation():
        if random.random() < 0.6:  # 60% failure rate
            raise ValueError("Slow operation failed")
        return "Slow operation succeeded"
    
    # Test fast operation
    print("\n1. Testing fast retry configuration:")
    try:
        result = fast_operation()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")
    
    # Test slow operation
    print("\n2. Testing slow retry configuration:")
    try:
        result = slow_operation()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")

def demonstrate_exception_filtering():
    """Demonstrate exception filtering"""
    print("\n=== Exception Filtering ===")
    
    # Retry only on specific exceptions
    @RetryMechanism(max_attempts=3, base_delay=0.2, 
                   exceptions=(ValueError, TypeError), log_file="filtered_retry.log")
    def selective_retry():
        error_type = random.choice([ValueError, TypeError, RuntimeError])
        raise error_type(f"Random {error_type.__name__} error")
    
    print("Testing selective retry (only retries ValueError and TypeError):")
    try:
        result = selective_retry()
        print(f"   Result: {result}")
    except Exception as e:
        print(f"   Final error: {e}")

def show_log_files():
    """Show the contents of log files"""
    print("\n=== Retry Log Files Contents ===")
    
    log_files = [
        "retry_attempts.log",
        "database_operations.log",
        "fast_retry.log",
        "slow_retry.log",
        "filtered_retry.log"
    ]
    
    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"\n{log_file}:")
            try:
                with open(log_file, 'r') as f:
                    content = f.read()
                    if content.strip():
                        print(content)
                    else:
                        print("   (Empty file)")
            except Exception as e:
                print(f"   Error reading file: {e}")
        else:
            print(f"\n{log_file}: (File not found)")

def main():
    """Main function to demonstrate the retry mechanism"""
    print("=== Retry Mechanism Decorator ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Run retry mechanism demonstration")
        print("2. Test different configurations")
        print("3. Test exception filtering")
        print("4. Show log files")
        print("5. Clear log files")
        print("6. Exit")
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                demonstrate_retry_mechanism()
            
            elif choice == '2':
                demonstrate_different_configurations()
            
            elif choice == '3':
                demonstrate_exception_filtering()
            
            elif choice == '4':
                show_log_files()
            
            elif choice == '5':
                log_files = [
                    "retry_attempts.log",
                    "database_operations.log",
                    "fast_retry.log",
                    "slow_retry.log",
                    "filtered_retry.log"
                ]
                for log_file in log_files:
                    if os.path.exists(log_file):
                        os.remove(log_file)
                        print(f"Removed {log_file}")
                print("All log files cleared.")
            
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