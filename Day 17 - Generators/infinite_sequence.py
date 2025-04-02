def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
print("First 5 Fibonacci:", [next(fib) for _ in range(5)])