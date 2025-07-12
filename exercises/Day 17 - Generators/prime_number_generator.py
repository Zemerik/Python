"""
Exercise 2: Prime Number Generator
Build a prime number generator that:
- Generates prime numbers on-demand
- Maintains state between calls
- Can generate infinite primes
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_generator():
    """Infinite generator for prime numbers"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def get_n_primes(n):
    """Get the first n prime numbers"""
    primes = []
    gen = prime_generator()
    for _ in range(n):
        primes.append(next(gen))
    return primes

def main():
    print("=== Prime Number Generator ===")
    gen = prime_generator()
    print("First 10 primes:")
    for _ in range(10):
        print(next(gen), end=' ')
    print("\nFirst 20 primes:", get_n_primes(20))
    # Demonstrate infinite generation (stop after 30th prime)
    print("\nPrimes up to 100:")
    gen = prime_generator()
    for p in gen:
        if p > 100:
            break
        print(p, end=' ')
    print()

if __name__ == "__main__":
    main() 