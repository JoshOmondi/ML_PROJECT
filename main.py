import pandas as pd

# Load IPL data
df = pd.read_csv("data.csv")

# Basic stats
print("Top Winners:")
print(df["winner"].value_counts())

print("\nPlayer of the Match Awards:")
print(df["player_of_match"].value_counts().head(5))
