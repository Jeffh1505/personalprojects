
# importing section 
import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import scipy as sp 


# using the Csv file 
df = pd.read_csv(r'C:\Users\summe\OneDrive\Desktop\personalprojects\MachineLearning\car data.csv')  
  
# Checking the first 5 entries of dataset 
df.head()