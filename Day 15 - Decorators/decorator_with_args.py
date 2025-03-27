def repeat(n=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=2)
def greet(name):
    print(f"Hello {name}")

greet("Joe")