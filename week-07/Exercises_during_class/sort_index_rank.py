# sort_index() and rank()

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
    "Score": [88, 95, 79, 91]
}, index=[3, 1, 2, 0])

print("ORIGINAL DATAFRAME")
print(df)

# Sort will change the order
print("\nSORTED INDEX")
print(df.sort_index())

df["Rank"] = df["Score"].rank(ascending=False)

# Rank will assign position or rank
print("\nWITH RANKINGS")
print(df)


print("\nSORTED INDEX (Highest to Lowest)")
sorted_df = df.sort_index(ascending=False)
print(sorted_df)

df["Rank"] = df["Score"].rank(ascending=False)

# Sort by rank so highest score appears first
ranked_df = df.sort_values(by="Rank")
print("\nRANKINGS (Highest to Lowest)")
print(ranked_df)
