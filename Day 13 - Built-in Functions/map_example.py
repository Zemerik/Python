# Basic map usage
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Multiple iterators
widths = [10, 20, 30]
heights = [5, 7, 9]
areas = list(map(lambda w, h: w * h, widths, heights))
print(f"Areas: {areas}")