import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
e = 1.602176634e-19  # Charge of electron (C)
m = 9.10938356e-31  # Mass of electron (kg)
N = 132  # Number of turns
R = 0.1475  # Radius of coil (m)

# Calculate the constant C
C = (mu_0 * N) / (R * (5/4)**(3/2))

# Load the Excel file (change the path if necessary)
file_path = r"C:\Users\summe\Downloads\columbiaphyslab5.xlsx"
data = pd.read_excel(file_path)

# Clean the data
cleaned_data = data.iloc[4:].dropna(how='all').reset_index(drop=True)

# Assign appropriate column names
cleaned_data.columns = ['Voltage_200V_Diameter', 'Current_200V', 'NaN1', 'Voltage_300V_Diameter', 'Current_300V', 
                        'NaN2', 'Voltage_400V_Diameter', 'Current_400V', 'NaN3', 'Voltage_500V_Diameter', 'Current_500V', 'NaN4']

# Extract diameters and amperes for each voltage group (convert diameters to radii in meters)
radius_200V = cleaned_data['Voltage_200V_Diameter'].astype(float) / 200  # Convert diameter (cm) to radius (m)
current_200V = cleaned_data['Current_200V'].astype(float)

radius_300V = cleaned_data['Voltage_300V_Diameter'].astype(float) / 200
current_300V = cleaned_data['Current_300V'].astype(float)

radius_400V = cleaned_data['Voltage_400V_Diameter'].astype(float) / 200
current_400V = cleaned_data['Current_400V'].astype(float)

radius_500V = cleaned_data['Voltage_500V_Diameter'].astype(float) / 200
current_500V = cleaned_data['Current_500V'].astype(float)

# Define the theoretical current function
def calculate_theoretical_current(V, r, C):
    return (1 / C) * np.sqrt((2 * V) / (e / m)) * (1 / r)

# Set voltage values for each dataset
V_200 = 200
V_300 = 300
V_400 = 400
V_500 = 500

# Calculate theoretical currents
theoretical_current_200V = calculate_theoretical_current(V_200, radius_200V, C)
theoretical_current_300V = calculate_theoretical_current(V_300, radius_300V, C)
theoretical_current_400V = calculate_theoretical_current(V_400, radius_400V, C)
theoretical_current_500V = calculate_theoretical_current(V_500, radius_500V, C)

# Plot the results
plt.figure(figsize=(10, 6))

plt.plot(radius_200V, current_200V, 'o-', label='200 V - Experimental')
plt.plot(radius_200V, theoretical_current_200V, 'x--', label='200 V - Theoretical')

plt.plot(radius_300V, current_300V, 'o-', label='300 V - Experimental')
plt.plot(radius_300V, theoretical_current_300V, 'x--', label='300 V - Theoretical')

plt.plot(radius_400V, current_400V, 'o-', label='400 V - Experimental')
plt.plot(radius_400V, theoretical_current_400V, 'x--', label='400 V - Theoretical')

plt.plot(radius_500V, current_500V, 'o-', label='500 V - Experimental')
plt.plot(radius_500V, theoretical_current_500V, 'x--', label='500 V - Theoretical')

# Adding plot details
plt.title("Current vs Radius for Different Voltages")
plt.xlabel("Radius (m)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
