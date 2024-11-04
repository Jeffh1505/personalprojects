import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Physical constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
N = 132     # Number of turns in the coil
R = 0.1475  # Radius of coil (m)
C = (mu_0 * N) / (R * (5/4)**(3/2))  # Geometric constant

# Data for different voltages (converting radius from cm to m)
def load_voltage_data(radius_cm, current_A):
    radius_m = np.array(radius_cm) / 100  # Convert to meters
    current = np.array(current_A)
    current_error = 0.05 * current  # 5% error
    return radius_m, current, current_error

# Weighted linear regression
def weighted_linear_regression(x, y, yerr):
    weights = 1 / yerr**2
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Calculate errors
    slope_err = np.sqrt(np.sum(weights * (x - np.mean(x))**2))
    intercept_err = std_err * np.sqrt(np.sum(weights))
    
    return slope, intercept, slope_err, intercept_err

# Calculate e/m ratio from slope
def charge_to_mass_from_slope(slope, V):
    return (2 * V) / (C * slope)**2

# Create plot
def plot_data_and_fits(data_sets, fits):
    plt.figure(figsize=(10, 6))
    colors = ['r', 'g', 'b', 'y']
    
    for (voltage, radius, current, current_error), fit, color in zip(data_sets, fits, colors):
        # Plot experimental points with error bars
        plt.errorbar(radius, current, yerr=current_error, 
                    fmt='o', label=f'{voltage}V - Experimental', 
                    capsize=5, color=color)
        
        # Plot fit line
        x_fit = np.linspace(min(radius), max(radius), 100)
        plt.plot(x_fit, fit[0] * x_fit + fit[1], 
                '--', label=f'{voltage}V - Fit', 
                color=color)
    
    plt.xlabel('Radius (m)')
    plt.ylabel('Current (A)')
    plt.title('Current vs Radius for Different Voltages with Best-Fit Lines')
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate LaTeX table
def create_latex_table(fits, voltages):
    latex_table = r"""
    \begin{table}[ht]
    \centering
    \begin{tabular}{|c|c|c|c|c|}
    \hline
    Voltage (V) & Slope (A/m) & Intercept (A) & Slope Error (A/m) & Intercept Error (A) \\ \hline
    """
    
    for voltage, fit in zip(voltages, fits):
        latex_table += f"{voltage} & {fit[0]:.2e} & {fit[1]:.2e} & {fit[2]:.2e} & {fit[3]:.2e} \\\\ \\hline\n"
    
    latex_table += r"""
    \end{tabular}
    \caption{Linear Fit Results for Current vs Radius.}
    \end{table}
    """
    return latex_table

# Main analysis
if __name__ == "__main__":
    # Complete datasets from original code
    data_sets = [
        (200, 
         [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11],
         [2.05, 1.83, 1.65, 1.54, 1.42, 1.34, 1.29, 1.21, 1.16, 1.12, 1.07, 1.02, 0.97]),
        (300,
         [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11],
         [2.66, 2.4, 2.12, 1.98, 1.86, 1.75, 1.62, 1.53, 1.44, 1.38, 1.32, 1.27, 1.22]),
        (400,
         [5.25, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11],
         [3, 2.89, 2.6, 2.4, 2.21, 2.03, 1.93, 1.81, 1.7, 1.61, 1.53, 1.46, 1.4]),
        (500,
         [6, 6, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11],
         [3, 2.96, 2.6, 2.71, 2.54, 2.36, 2.2, 2.06, 1.94, 1.82, 1.71, 1.64, 1.56])
    ]
    
    # Process each dataset
    processed_data = []
    fits = []
    em_ratios = []
    voltages = []
    
    for voltage, radius_cm, current_A in data_sets:
        radius, current, current_error = load_voltage_data(radius_cm, current_A)
        fit = weighted_linear_regression(radius, current, current_error)
        
        processed_data.append((voltage, radius, current, current_error))
        fits.append(fit)
        voltages.append(voltage)
        
        em_ratio = charge_to_mass_from_slope(fit[0], voltage)
        em_ratios.append(em_ratio)
    
    # Calculate weighted average
    em_ratios = np.array(em_ratios)
    errors = np.array([fit[2] for fit in fits])
    weights = 1 / errors**2
    weighted_avg = np.sum(em_ratios * weights) / np.sum(weights)
    weighted_std_err = np.sqrt(1 / np.sum(weights))
    
    # Print results
    print("\nWeighted Average of Charge-to-Mass Ratio: {:.2e} C/kg".format(weighted_avg))
    print("Weighted Standard Error: {:.2e} C/kg".format(weighted_std_err))
    
    # Generate and print LaTeX table
    latex_table = create_latex_table(fits, voltages)
    print("\nLaTeX Table for Linear Fit Results:")
    print(latex_table)
    
    # Plot results
    plot_data_and_fits(processed_data, fits)