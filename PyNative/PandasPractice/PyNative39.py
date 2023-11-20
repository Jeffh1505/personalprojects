import pandas as pd 


df = pd.read_csv(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PyNative\PandasPractice\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)
