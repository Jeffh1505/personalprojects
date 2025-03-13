import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv(r"C:\Users\summe\OneDrive\Desktop\personalprojects\ORCA Practice\sales_data.csv")

# Display first 5 rows
print(df.head())

df = df.assign(Final_price = df["Price"] - (df["Price"]*df["Discount"]))
print(df)

print(df.loc[df["Final_price"] > 500, ["Final_price"]])

sorted_df = df.sort_values(by="Revenue", ascending=False)
print(sorted_df)


print(df.loc[df["Quantity"] > 3, ["Quantity"]])