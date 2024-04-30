import pandas as pd
import re

def find_highest_voltages(filename):
    # Read the data into a DataFrame
    df = pd.read_csv(filename, delimiter='\t', skiprows=1, header=None, names=['Frequency', 'Voltage'])
    
    # Extract numerical voltage values using regular expressions
    voltage_pattern = r'\((-?\d+\.\d+)'
    df['Voltage'] = df['Voltage'].str.extract(voltage_pattern).astype(float)
    
    # Find the highest two voltages and their corresponding frequencies
    highest_voltages = df.nlargest(2, 'Voltage')
    
    return highest_voltages['Voltage'].values, highest_voltages['Frequency'].values

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    highest_voltages, highest_frequencies = find_highest_voltages(filename)
    print("Highest Output Voltages and Corresponding Frequencies:")
    for voltage, frequency in zip(highest_voltages, highest_frequencies):
        print("Voltage:", voltage, "Frequency:", frequency)
