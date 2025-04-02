# Day 17: Generators

## What You'll Learn:
- Creating generator functions with `yield`
- Understanding lazy evaluation
- Memory-efficient iteration
- Generator expressions vs list comprehensions
- Pipeline processing with generators

## Files:
1. `generator_basics.py` - Simple generator function
2. `generator_expression.py` - Generator expressions
3. `infinite_sequence.py` - Infinite generators
4. `pipeline.py` - Chaining generators

## Exercises:
1. Create a log file processor that:
   - Reads large log files line-by-line using generators
   - Filters lines containing "ERROR"
   - Yields formatted error messages

2. Build a prime number generator that:
   - Generates prime numbers on-demand
   - Maintains state between calls
   - Can generate infinite primes