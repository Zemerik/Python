import pandas as pd

# From dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Paris", "London", "Berlin"]
}
df = pd.DataFrame(data)
print("From Dictionary:\n", df)

# From list of lists
data = [
    [100, "Widget A", 19.99],
    [101, "Widget B", 29.99],
    [102, "Widget C", 39.99]
]
df = pd.DataFrame(data, columns=["ID", "Product", "Price"])
print("\nFrom Lists:\n", df)