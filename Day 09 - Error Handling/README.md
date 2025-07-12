# Day 9: Error Handling

## What You'll Learn:
- Handling exceptions with `try/except`
- Using `finally` for cleanup operations
- Raising custom exceptions
- Built-in exception types

## Files:
1. `basic_try_except.py` - Simple error catching
2. `specific_exceptions.py` - Handling different error types
3. `finally_usage.py` - Cleanup operations
4. `raising_exceptions.py` - Custom error raising

## Exercises:
1. Create a number input validator that:
   - Keeps asking for input until valid number
   - Handles both ValueError and KeyboardInterrupt
   - Prints "Thank you!" on successful input

2. Build a file reader that:
   - Gracefully handles missing files
   - Shows different messages for different error types
   - Always closes file resources