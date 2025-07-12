# Set creation
primes = {2, 3, 5, 7, 11}
evens = {2, 4, 6, 8}

# Set methods
primes.add(13)
primes.discard(2)

# Mathematical operations
print("Union:", primes | evens)
print("Intersection:", primes & evens)
print("Difference:", primes - evens)

# Membership test
print(7 in primes)  # True