import pandas as pd
import numpy as np

# Create sample data with missing values
data = {
    "A": [1, 2, np.nan, 4],
    "B": ["X", np.nan, "Z", "W"],
    "C": [0.1, 0.2, 0.3, np.nan]
}
df = pd.DataFrame(data)

# Handle missing data
print("Original:\n", df)
print("\nDrop NA:\n", df.dropna())
print("\nFill NA:\n", df.fillna(method="ffill"))

# Type conversion
df["A"] = df["A"].astype("Int64")
print("\nFixed Types:\n", df.dtypes)