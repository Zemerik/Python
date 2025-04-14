import pandas as pd

# Write to CSV
data = {"Temperature": [22.1, 23.5, 19.8], "Humidity": [45, 62, 38]}
df = pd.DataFrame(data)
df.to_csv("weather.csv", index=False)

# Read from CSV
df = pd.read_csv("weather.csv")
print("CSV Data:\n", df)

# Append to CSV
new_data = pd.DataFrame({"Temperature": [21.3], "Humidity": [55]})
new_data.to_csv("weather.csv", mode="a", header=False, index=False)