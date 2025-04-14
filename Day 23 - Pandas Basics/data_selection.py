import pandas as pd

df = pd.read_csv("weather.csv")

# Column selection
print("Humidity Column:\n", df["Humidity"])

# Row filtering
print("High Humidity:\n", df[df["Humidity"] > 50])

# loc/iloc
print("First Row:\n", df.iloc[0])
print("Temp > 20:\n", df.loc[df["Temperature"] > 20])