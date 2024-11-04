import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
N = 132  # Number of turns
R = 0.1475  # Radius of coil (m)
C = (mu_0 * N) / (R * (5/4)**(3/2))  # Calculate the constant C

# Provided data (Radius in cm, Current in A)
radius_200V = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]) / 100  # Convert to meters
current_200V = np.array([2.05, 1.83, 1.65, 1.54, 1.42, 1.34, 1.29, 1.21, 1.16, 1.12, 1.07, 1.02, 0.97])

radius_300V = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]) / 100  # Convert to meters
current_300V = np.array([2.66, 2.4, 2.12, 1.98, 1.86, 1.75, 1.62, 1.53, 1.44, 1.38, 1.32, 1.27, 1.22])

radius_400V = np.array([5.25, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]) / 100  # Convert to meters
current_400V = np.array([3, 2.89, 2.6, 2.4, 2.21, 2.03, 1.93, 1.81, 1.7, 1.61, 1.53, 1.46, 1.4])

radius_500V = np.array([6, 6, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]) / 100  # Convert to meters
current_500V = np.array([3, 2.96, 2.6, 2.71, 2.54, 2.36, 2.2, 2.06, 1.94, 1.82, 1.71, 1.64, 1.56])

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
print(f"200 V: {e_m_200V.mean():.2e} C/kg")
print(f"300 V: {e_m_300V.mean():.2e} C/kg")
print(f"400 V: {e_m_400V.mean():.2e} C/kg")
print(f"500 V: {e_m_500V.mean():.2e} C/kg")

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

# Plotting the experimental and theoretical current vs radius
def calculate_theoretical_current(V, r, C, e_m):
    return (1 / C) * np.sqrt((2 * V) / e_m) * (1 / r)

# Calculate theoretical currents using the mean charge-to-mass ratio from the 200V data
theoretical_current_200V = calculate_theoretical_current(V_200, radius_200V, C, e_m_200V.mean())
theoretical_current_300V = calculate_theoretical_current(V_300, radius_300V, C, e_m_300V.mean())
theoretical_current_400V = calculate_theoretical_current(V_400, radius_400V, C, e_m_400V.mean())
theoretical_current_500V = calculate_theoretical_current(V_500, radius_500V, C, e_m_500V.mean())

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
