"""
Exercise 1: Faulty Factorial Debugging
Debug a faulty function that:
- Miscalculates factorial values
- Fails on specific inputs
- Use pdb to identify logic errors
(Include comments for breakpoints and investigation.)
"""

def faulty_factorial(n):
    # Intentional bug: should be n * factorial(n-1), but uses n + factorial(n-1)
    if n < 0:
        raise ValueError('Negative input not allowed')
    if n == 0:
        return 1
    return n + faulty_factorial(n-1)  # <-- LOGIC ERROR HERE

def main():
    import pdb; pdb.set_trace()  # Set a breakpoint here
    try:
        print('5! =', faulty_factorial(5))
        print('0! =', faulty_factorial(0))
        print('-1! =', faulty_factorial(-1))
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main() 