import csv
import numpy as np
import matplotlib as plt 

month_list = []
profit_list = []
with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PyNative\MatplotlibPractice\company_sales_data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        month = row[0]
        total_profit = row[8]
        if month.isnumeric() == True:
            month_list.append(int(month))
            profit_list.append(int(total_profit))
        
month_array = np.array(month_list[1:]).reshape(12,1)
profit_array = np.array(profit_list[1:])
print(profit_array)