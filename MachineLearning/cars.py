
# importing section 
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy as sp 


# using the Csv file 
df = pd.read_csv(r'C:\Users\summe\OneDrive\Desktop\personalprojects\MachineLearning\car data.csv')  
  
# Checking the first 5 entries of dataset 


headers = ["symboling", "normalized-losses", "make",  
           "fuel-type", "aspiration","num-of-doors", 
           "body-style","drive-wheels", "engine-location", 
           "wheel-base","length", "width","height", "curb-weight", 
           "engine-type","num-of-cylinders", "engine-size",  
           "fuel-system","bore","stroke", "compression-ratio", 
           "horsepower", "peak-rpm","city-mpg","highway-mpg","price"] 
  
df.columns=headers 
print(df.head()) 