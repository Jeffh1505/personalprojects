import pandas as pd
df = pd.read_csv(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PyNative\PandasPractice\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers[['company','average-mileage']].mean()
print(mileageDf)