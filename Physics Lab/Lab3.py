import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Charging data for capacitors (in microamps)
ten_microfarad_charging = [15, 10, 8, 6, 5, 4.5, 4, 3, 2, 2]
twenty_microfarad_charging = [14, 10.25, 9.85, 9, 8, 7, 6, 5.75, 5.25, 5]
thirty_microfarad_charging = [15, 10, 9.5, 9.0, 8.75, 8.25, 7.75, 7.25, 7, 6.75]

# Discharging data for capacitors (in microamps)
ten_microfarad_discharging = [13.75, 8, 6.25, 5.5, 3, 2.75, 2, 1.75, 1.25, 1]
twenty_microfarad_discharging = [9, 8, 7, 5, 4.95, 4, 3.75, 3.25, 3, 2.75]
thirty_microfarad_discharging = [10, 9.25, 7.95, 6.85, 6.5, 6, 5.25, 5, 4.75, 4.1]

def linearize(L: list):
    """Linearize the data by applying natural log"""
    new_list = np.array(L)
    return np.log(new_list)

def funclin(x, a, b):
    """Linear function for fitting"""
    return a + b * x

def to_latex_table(data: list, columns: list, caption: str, label: str) -> str:
    table_str = "\\begin{table}[ht]\n\\centering\n\\begin{tabular}{|" + "c|" * len(columns) + "}\n\\hline\n"
    table_str += " & ".join(columns) + " \\\\ \\hline\n"
        
    for row in zip(*data):
        table_str += " & ".join(f"{float(item):.2f}" if isinstance(item, (float, np.float64, np.int64)) else str(item) for item in row) + " \\\\ \\hline\n"
        
    table_str += "\\end{tabular}\n"
    table_str += f"\\caption{{{caption}}}\n"
    table_str += f"\\label{{{label}}}\n"
    table_str += "\\end{table}\n"
    return table_str

# Limit data to first 10 points
ten_microfarad_charging = ten_microfarad_charging[:10]
twenty_microfarad_charging = twenty_microfarad_charging[:10]
thirty_microfarad_charging = thirty_microfarad_charging[:10]

ten_microfarad_discharging = ten_microfarad_discharging[:10]
twenty_microfarad_discharging = twenty_microfarad_discharging[:10]
thirty_microfarad_discharging = thirty_microfarad_discharging[:10]

# Linearize the charging data
charging = [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]
linearized_charging = [linearize(charging_list) for charging_list in charging]

# Linearize the discharging data
discharging = [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]
linearized_discharging = [linearize(discharging_list) for discharging_list in discharging]

# Time in seconds (first 10 points)
time_data = [np.arange(10)] * 3  # Assuming 1 second intervals for each dataset

# Error is 10% of the data values
error_charging = [np.array(data) * 0.10 for data in charging]
error_discharging = [np.array(data) * 0.10 for data in discharging]

# Constants
R_load = 510e3  # Load resistance in ohms (510 kΩ)
tolerance = 0.10  # ±10% tolerance

# Capacitances in farads
capacitances = [10e-6, 20e-6, 30e-6]  # 10µF, 20µF, 30µF

# Store total resistances and internal resistances for charging
total_resistances_charging = []
internal_resistances_charging = []

# Plot and fit each dataset on separate graphs for charging and calculate internal resistance
for i, (time, data, error) in enumerate(zip(time_data, linearized_charging, error_charging)):
    # Perform the curve fitting and get parameters
    params, cov = opt.curve_fit(funclin, time, data, sigma=error, absolute_sigma=True)
    slope = params[1]  # Slope (1/RC)

    # Calculate total resistance (R_total) using slope and capacitance
    C = capacitances[i]
    R_total = -1 / (slope * C)  # R_total = -1/(slope * C)

    # Include tolerance when calculating internal resistance
    R_total_tolerance = R_total * (1 + tolerance)  # Max total resistance with tolerance
    R_internal = R_total_tolerance - R_load  # R_internal = R_total - R_load

    total_resistances_charging.append(R_total)
    internal_resistances_charging.append(R_internal)

    # Print results for each capacitance
    print(f"For {C * 1e6}µF (Charging):")
    print(f"  Slope (1/RC) = {slope:.5f}")
    print(f"  Total Resistance (R_total) = {R_total / 1e3:.2f} kΩ")
    print(f"  Internal Resistance (R_internal) = {R_internal / 1e3:.2f} kΩ")
    
    # Generate best fit line
    fit_line = funclin(time, *params)
    
    # Create a new figure for each dataset
    plt.figure()

    # Plot the linearized data with error bars
    plt.errorbar(time, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Charging)', capsize=3, elinewidth=1, markeredgewidth=1)

    # Plot the best fit line
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF (Charging)', color='red')

    # Customize the plot
    plt.title(f'Linearized Charging Data with Best Fit {(i+1)*10}µF')
    plt.xlabel('Time (seconds)')
    plt.ylabel('ln(Current) (µA)')
    plt.legend()
    plt.grid(True)
    slope_text = f"Slope (1/RC) = {params[1]:.2f}"
    plt.text(0.002, min(data) + 0.001, slope_text, fontsize=12, color='green')
    
    # Show the plot
    plt.show()

# Prepare data for LaTeX table (Capacitance, Total Resistance, Internal Resistance for Charging)
cap_values = [f"{C * 1e6} µF" for C in capacitances]
total_resistances_charging_kohms = [R_total / 1e3 for R_total in total_resistances_charging]
internal_resistances_charging_kohms = [R_internal / 1e3 for R_internal in internal_resistances_charging]

# Calculate mean and standard error of the total resistances and internal resistances for Charging
mean_total_R_charging = np.mean(total_resistances_charging_kohms)
mean_internal_R_charging = np.mean(internal_resistances_charging_kohms)
standard_error_total_R_charging = np.std(total_resistances_charging_kohms) / np.sqrt(len(total_resistances_charging_kohms))
standard_error_internal_R_charging = np.std(internal_resistances_charging_kohms) / np.sqrt(len(internal_resistances_charging_kohms))

# Append the mean and standard error to the data for Charging
cap_values.append("Mean")
cap_values.append("Standard Error")
total_resistances_charging_kohms.append(mean_total_R_charging)
total_resistances_charging_kohms.append(standard_error_total_R_charging)
internal_resistances_charging_kohms.append(mean_internal_R_charging)
internal_resistances_charging_kohms.append(standard_error_internal_R_charging)

# LaTeX table columns and data for Charging
columns = ["Capacitance", "Total Resistance (kΩ)", "Internal Resistance (kΩ)"]
latex_table_charging = to_latex_table(
    [cap_values, total_resistances_charging_kohms, internal_resistances_charging_kohms],
    columns, caption="Calculated Resistances for Each Capacitance (Charging)", label="resistance_table_charging"
)
print(latex_table_charging)

# Store total resistances for discharging
total_resistances_discharging = []

# Plot and fit each dataset on separate graphs for discharging and calculate total resistance
for i, (time, data, error) in enumerate(zip(time_data, linearized_discharging, error_discharging)):
    # Perform the curve fitting and get parameters
    params, cov = opt.curve_fit(funclin, time, data, sigma=error, absolute_sigma=True)
    slope = params[1]  # Slope (1/RC)

    # Calculate total resistance (R_total) using slope and capacitance
    C = capacitances[i]
    R_total = -1 / (slope * C)  # R_total = -1/(slope * C)

    total_resistances_discharging.append(R_total)

    # Print results for each capacitance
    print(f"For {C * 1e6}µF (Discharging):")
    print(f"  Slope (1/RC) = {slope:.5f}")
    print(f"  Total Resistance (R_total) = {R_total / 1e3:.2f} kΩ")

    # Generate best fit line
    fit_line = funclin(time, *params)
    
    # Create a new figure for each dataset
    plt.figure()

    # Plot the linearized data with error bars
    plt.errorbar(time, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Discharging)', capsize=3, elinewidth=1, markeredgewidth=1)

    # Plot the best fit line
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF (Discharging)', color='red')

    # Customize the plot
    plt.title(f'Linearized Discharging Data with Best Fit {(i+1)*10}µF')
    plt.xlabel('Time (seconds)')
    plt.ylabel('ln(Current) (µA)')
    plt.legend()
    plt.grid(True)
    slope_text = f"Slope (1/RC) = {params[1]:.2f}"
    plt.text(0.002, min(data) + 0.001, slope_text, fontsize=12, color='green')
    
    # Show the plot
    plt.show()

# Prepare data for LaTeX table (Capacitance, Total Resistance for Discharging)
total_resistances_discharging_kohms = [R_total / 1e3 for R_total in total_resistances_discharging]

# Calculate mean and standard error of the total resistances for Discharging
mean_total_R_discharging = np.mean(total_resistances_discharging_kohms)
standard_error_total_R_discharging = np.std(total_resistances_discharging_kohms) / np.sqrt(len(total_resistances_discharging_kohms))

# Append the mean and standard error to the data for Discharging
total_resistances_discharging_kohms.append(mean_total_R_discharging)
total_resistances_discharging_kohms.append(standard_error_total_R_discharging)

# LaTeX table columns and data for Discharging
columns_discharging = ["Capacitance", "Total Resistance (kΩ)"]
latex_table_discharging = to_latex_table(
    [cap_values, total_resistances_discharging_kohms],
    columns_discharging, caption="Calculated Resistances for Each Capacitance (Discharging)", label="resistance_table_discharging"
)
print(latex_table_discharging)
