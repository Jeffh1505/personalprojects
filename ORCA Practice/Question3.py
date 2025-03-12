import pandas as pd

df = pd.DataFrame({
    "A": [10, 15, 7, 20, 25],
    "B": [30, 12, 45, 18, 22],
    "C": [5, 8, 10, 2, 6]
})
df = df.assign(total= df["A"] + df["B"])
print(df)