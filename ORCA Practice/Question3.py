import pandas as pd

df = pd.DataFrame({
    "A": [10, 15, 7, 20, 25],
    "B": [30, 12, 45, 18, 22],
    "C": [5, 8, 10, 2, 6]
})

df = df.assign(total= df["A"] + df["B"])
print(df)

print(df.loc[df["A"] > 10, :])
print(df.loc[df["B"] < 25, :])

df = df.sort_values(by=["C"], ascending=True)
df = df.sort_values(by=["A"], ascending=False)

print(df)
