# Contribution Guidelines

Thank you for considering contributing to this 30-day Python learning project! To maintain consistency and quality, please follow these guidelines:

## 🧹 Code Quality Standards

### 1. Readability First

- Follow PEP 8 style guide
- Use descriptive variable/function names

```python
# Good
def calculate_average(numbers):
  
# Avoid
def avg(lst):
```

### 2. Modular Code

- Keep functions focused (single responsibility principle)

- Limit functions to 15 lines maximum

- Split large files into logical modules

### 3. Documentation

**For code:**

- Use Python docstrings for all functions/classes

```python
def convert_temperature(celsius):
    """
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32
```

**For Projects:**

- Update README.md in each folder with:

    - Purpose of the code

    - Usage examples

    - Dependencies

    - Learning objectives

## 📝 Contribution Process:

1. **Fork** the repository

2. Create a **feature branch:**

```
git checkout -b feat/add-day7-exercises
```

3. Follow the project structure:

    - One concept per file

    - Group related files in day folders

    - Keep examples self-contained

4. **Test** your code:

    - All examples should run with `python filename.py`

    - Include test cases where applicable

5. Commit with descriptive messages:

```
git commit -m "feat: add dictionary examples to Day 7"
```

6. **Pull Request**:

    - Reference related issues

    - Include before/after screenshots if UI changes

    - Describe your changes in detail

## 🚫 What to Avoid

- Monolithic code blocks

- Uncommented complex logic

- Duplicate code between files

- Platform-specific solutions without alternatives

## 📚 Documentation Standards

**In-Code Comments**

- Use `#` comments sparingly for non-obvious logic

```python
# Using Sieve of Eratosthenes algorithm
def find_primes(n):
    ...
```

**Project Documentation**

- Update both root and folder-level READMEs

- Use consistent Markdown formatting

- Add visual aids (code snippets, diagrams) where helpful

## 💡 Helpful Tips

- Use flake8 for code `linting`

- Run black for consistent `formatting`

- Verify documentation with `pydocstyle`

## ❓ Need Help?

Open an issue for:

- Clarification requests

- Feature suggestions

- Reporting bugs

Let's build an accessible learning resource together! 🐍

_ _ _

- 📢 “Great things in programming are never done by one person. They’re done by a team of people.” – Inspired by Steve Jobs