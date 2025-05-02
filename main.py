import pandas as pd

# Create and save test data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "Location": ["Nairobi", "Accra", "Johannesburg"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

# Now read it back
df_read = pd.read_csv("data.csv")
print(df_read)
