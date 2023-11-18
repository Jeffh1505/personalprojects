import csv
import numpy as np
import matplotlib as plt 
month_array = np.zeros((3,4), dtype="uint8") 
with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PyNative\MatplotlibPractice\company_sales_data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        month,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,total_units,total_profit = row
        month_array = np.concatenate(month)

print(month_array)