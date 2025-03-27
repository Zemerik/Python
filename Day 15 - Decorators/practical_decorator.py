import functools

def cache(func):
    """Memoization decorator"""
    stored = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in stored:
            stored[args] = func(*args)
        return stored[args]
    return wrapper

def require_auth(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.is_authenticated:
            return func(user, *args, **kwargs)
        raise PermissionError("Login required")
    return wrapper

# Usage example
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))