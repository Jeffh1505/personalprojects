import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"]
})

df2 = pd.DataFrame({
    "ID": [3, 4, 5, 6],
    "Score": [85, 90, 78, 88]
})

new_df = pd.merge(df1, df2,how="outer")
print(new_df)