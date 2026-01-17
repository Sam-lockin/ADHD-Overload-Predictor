import pandas as pd

# Load the CSV
df = pd.read_csv("data/overload_log.csv")

# Show basic info
print("=== First 5 Rows ===")
print(df.head())

print("\n=== Column Info ===")
print(df.info())

print("\n=== Unique Overload Levels ===")
print(df['overload_level'].unique())
