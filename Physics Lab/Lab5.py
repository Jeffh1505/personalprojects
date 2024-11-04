import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
N = 132  # Number of turns
R = 0.1475  # Radius of coil (m)
C = (mu_0 * N) / (R * (5/4)**(3/2))  # Calculate the constant C

# Load the Excel file (change the path if necessary)
file_path = r"C:\Users\summe\Downloads\columbiaphyslab5.xlsx"
data = pd.read_excel(file_path)

# Clean the data
cleaned_data = data.iloc[4:].dropna(how='all').reset_index(drop=True)

# Check the number of columns in the data
cleaned_data.columns = ['Voltage_200V_Diameter', 'Current_200V', 'NaN1', 'Voltage_300V_Diameter', 'Current_300V', 
                        'NaN2', 'Voltage_400V_Diameter', 'Current_400V', 'NaN3', 'Voltage_500V_Diameter', 'Current_500V', 'NaN4', 'NaN5']
cleaned_data = cleaned_data.drop(columns=['NaN1', 'NaN2', 'NaN3', 'NaN4', 'NaN5'])

# Extract diameters and amperes for each voltage group (convert diameters to radii in meters)
radius_200V = cleaned_data['Voltage_200V_Diameter'].astype(float) / 200  # Convert diameter (cm) to radius (m)
current_200V = cleaned_data['Current_200V'].astype(float)

radius_300V = cleaned_data['Voltage_300V_Diameter'].astype(float) / 200
current_300V = cleaned_data['Current_300V'].astype(float)

radius_400V = cleaned_data['Voltage_400V_Diameter'].astype(float) / 200
current_400V = cleaned_data['Current_400V'].astype(float)

radius_500V = cleaned_data['Voltage_500V_Diameter'].astype(float) / 200
current_500V = cleaned_data['Current_500V'].astype(float)

# Define the charge-to-mass ratio function
def calculate_charge_to_mass_ratio(V, I, r, C):
    return (2 * V) / (C * I * r)**2

# Set voltage values for each dataset
V_200 = 200
V_300 = 300
V_400 = 400
V_500 = 500

# Calculate charge-to-mass ratios for each voltage
e_m_200V = calculate_charge_to_mass_ratio(V_200, current_200V, radius_200V, C)
e_m_300V = calculate_charge_to_mass_ratio(V_300, current_300V, radius_300V, C)
e_m_400V = calculate_charge_to_mass_ratio(V_400, current_400V, radius_400V, C)
e_m_500V = calculate_charge_to_mass_ratio(V_500, current_500V, radius_500V, C)

# Print the charge-to-mass ratios
print("Charge-to-Mass Ratio (e/m) values:")
print(f"200 V: {e_m_200V.mean()} C/kg")
print(f"300 V: {e_m_300V.mean()} C/kg")
print(f"400 V: {e_m_400V.mean()} C/kg")
print(f"500 V: {e_m_500V.mean()} C/kg")

# Create LaTeX table with charge-to-mass ratio results
latex_table = r"""
\begin{table}[ht]
\centering
\begin{tabular}{|c|c|}
\hline
Voltage (V) & Charge-to-Mass Ratio (e/m) [C/kg] \\ \hline
200 & {:.2e} \\ \hline
300 & {:.2e} \\ \hline
400 & {:.2e} \\ \hline
500 & {:.2e} \\ \hline
\end{tabular}
\caption{Calculated charge-to-mass ratios at different voltages.}
\end{table}
""".format(e_m_200V.mean(), e_m_300V.mean(), e_m_400V.mean(), e_m_500V.mean())

# Output LaTeX table
print("\nLaTeX Table for Charge-to-Mass Ratio:")
print(latex_table)

# Optionally save the LaTeX table to a file
with open("charge_to_mass_ratio_table.tex", "w") as f:
    f.write(latex_table)

# Plotting the experimental and theoretical current vs radius
def calculate_theoretical_current(V, r, C):
    return (1 / C) * np.sqrt((2 * V) / (e_m_200V.mean())) * (1 / r)

# Calculate theoretical currents
theoretical_current_200V = calculate_theoretical_current(V_200, radius_200V, C)
theoretical_current_300V = calculate_theoretical_current(V_300, radius_300V, C)
theoretical_current_400V = calculate_theoretical_current(V_400, radius_400V, C)
theoretical_current_500V = calculate_theoretical_current(V_500, radius_500V, C)

# Plot the results
plt.figure(figsize=(10, 6))

# 200V plot
plt.plot(radius_200V, current_200V, 'o-', label='200 V - Experimental')
plt.plot(radius_200V, theoretical_current_200V, 'x--', label='200 V - Theoretical')

# 300V plot
plt.plot(radius_300V, current_300V, 'o-', label='300 V - Experimental')
plt.plot(radius_300V, theoretical_current_300V, 'x--', label='300 V - Theoretical')

# 400V plot
plt.plot(radius_400V, current_400V, 'o-', label='400 V - Experimental')
plt.plot(radius_400V, theoretical_current_400V, 'x--', label='400 V - Theoretical')

# 500V plot
plt.plot(radius_500V, current_500V, 'o-', label='500 V - Experimental')
plt.plot(radius_500V, theoretical_current_500V, 'x--', label='500 V - Theoretical')

# Adding plot details
plt.title("Current vs Radius for Different Voltages")
plt.xlabel("Radius (m)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show plot
plt.savefig("current_vs_radius_plot.png")
plt.show()
