import pandas as pd 


df = pd.read_csv(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PyNative\PandasPractice\Automobile_data.csv")
car_Manufacturers = df.groupby('company')

print(car_Manufacturers.describe())