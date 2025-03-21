# Day 10: Modules and Namespaces

## What You'll Learn:
- Importing built-in and custom modules
- Using `import` vs `from...import`
- Understanding `__name__` and script execution
- Creating reusable module files

## Files:
1. `basic_import.py` - Standard library imports
2. `name_usage.py` - __name__ demonstration
3. `module_usage.py` - Using custom modules

## Exercises:
1. Create a `math_utils.py` module with:
   - Function to calculate circle area (πr²)
   - Function to generate Fibonacci sequence
   - Test code using `if __name__ == "__main__"`

2. Build a temperature conversion package:
   - Create `temperature.py` with C/F/K conversions
   - Import it in `weather_report.py`
   - Handle different measurement systems