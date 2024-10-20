import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Charging data for capacitors (in microamps)
ten_microfarad_charging = [15, 10, 8, 6, 5, 4.5, 4, 3, 2, 2, 2, 1.5, 1.25, 1, 1, 1, 1, 1, 0.8, 0.5, 0.5, 0.4, 0.4, 0.3, 0.25, 0.20, 0.15, 0.1, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01]
twenty_microfarad_charging = [14, 10.25, 9.85, 9, 8, 7, 6, 5.75, 5.25, 5, 4.75, 4, 3.95, 3.25, 3.05, 3, 2.85, 2.75, 2.25, 2, 1.95, 1.85, 1.75, 1.65, 1.5, 1.45, 1.25, 1.05, 1.01, 1.0, 1.0, 1.0, 1, 1, 0.85, 0.85, 0.8, 0.8, 0.75, 0.75, 0.65, 0.6, 0.5, 0.5, 0.5, 0.5, 0.25]
thirty_microfarad_charging = [15, 10, 9.5, 9.0, 8.75, 8.25, 7.75, 7.25, 7, 6.75, 6, 5.75, 5.5, 5.1, 5, 4.75, 4.5, 4.05, 4, 3.85, 3.5, 3.25, 3, 3, 2.95, 2.85, 2.65, 2.5, 2.45, 2.25, 2.1, 2.05, 2, 1.95, 1.85, 1.75, 1.65, 1.5, 1.45, 1.35, 1.25, 1.15, 1.1, 1.05, 1.01, 1, 1, 1, 1, 1, 1, 1, 1, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.1]

# Discharging data for capacitors (in microamps)
ten_microfarad_discharging = [13.75, 8, 6.25, 5.5, 3, 2.75, 2, 1.75, 1.25, 1, 0.95, 0.9, 0.85, 0.75, 0.5, 0.45, 0.35, 0.25, 0.2, 0.1]
twenty_microfarad_discharging = [9, 8, 7, 5, 4.95, 4, 3.75, 3.25, 3, 2.75]
thirty_microfarad_discharging = [10, 9.25, 7.95, 6.85, 6.5, 6, 5.25, 5, 4.75, 4.1]

def linearize(L: list):
    """Linearize the data by applying natural log"""
    new_list = np.array(L)
    return np.log(new_list)

def funclin(x, a, b):
    """Linear function for fitting"""
    return a + b * x

# Limit data to first 10 points
ten_microfarad_charging = ten_microfarad_charging[:10]
twenty_microfarad_charging = twenty_microfarad_charging[:10]
thirty_microfarad_charging = thirty_microfarad_charging[:10]

ten_microfarad_discharging = ten_microfarad_discharging[:10]
twenty_microfarad_discharging = twenty_microfarad_discharging[:10]
thirty_microfarad_discharging = thirty_microfarad_discharging[:10]

# Linearize the charging and discharging data
charging = [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]
discharging = [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]

linearized_charging = [linearize(charging_list) for charging_list in charging]
linearized_discharging = [linearize(discharging_list) for discharging_list in discharging]

# Time in seconds (first 10 points)
time_ten = np.arange(10)  # assuming 1 second intervals
time_twenty = np.arange(10)
time_thirty = np.arange(10)

# Store time lists for each data set
time_data = [time_ten, time_twenty, time_thirty]

# Error is 10% of the data values
error_ten_charging = np.array(ten_microfarad_charging) * 0.10
error_twenty_charging = np.array(twenty_microfarad_charging) * 0.10
error_thirty_charging = np.array(thirty_microfarad_charging) * 0.10

error_ten_discharging = np.array(ten_microfarad_discharging) * 0.10
error_twenty_discharging = np.array(twenty_microfarad_discharging) * 0.10
error_thirty_discharging = np.array(thirty_microfarad_discharging) * 0.10

# Plot and fit each dataset on separate graphs for charging
for i, (time, data, error) in enumerate(zip(time_data, linearized_charging, [error_ten_charging, error_twenty_charging, error_thirty_charging])):
    # Perform the curve fitting
    params, _ = opt.curve_fit(funclin, time, data)

    # Generate best fit line
    fit_line = funclin(time, *params)
    
    # Create a new figure for each dataset
    plt.figure()

    # Plot the linearized data with error bars (10% error)
    plt.errorbar(time, data, yerr=error * 0.10, fmt='o', label=f'Charging Data Set {(i+1)*10}µF', capsize=3, elinewidth=1, markeredgewidth=1)

    # Plot the best fit line
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF', color='red')

    # Customize the plot
    plt.title(f'Linearized Charging Data with Best Fit {(i+1)*10}µF')
    plt.xlabel('Time (seconds)')
    plt.ylabel('ln(Current) (µA)')
    plt.legend()
    plt.grid(True)
    slope_text = f"Slope (1/RC) = {params[1]}"
    plt.text(0.002, min(data) + 0.001, slope_text, fontsize=12, color='green')
    

    # Show the plot
    plt.show()

# Plot and fit each dataset on separate graphs for discharging
for i, (time, data, error) in enumerate(zip(time_data, linearized_discharging, [error_ten_discharging, error_twenty_discharging, error_thirty_discharging])):
    # Perform the curve fitting
    params, _ = opt.curve_fit(funclin, time, data)

    # Generate best fit line
    fit_line = funclin(time, *params)
    
    # Create a new figure for each dataset
    plt.figure()

    # Plot the linearized data with error bars (10% error)
    plt.errorbar(time, data, yerr=error * 0.10, fmt='o', label=f'Discharging Data Set {(i+1)*10}µF', capsize=3, elinewidth=1, markeredgewidth=1)

    # Plot the best fit line
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF', color='red')

    # Customize the plot
    plt.title(f'Linearized Discharging Data with Best Fit (Discharging Set {(i+1)*10}µF)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('ln(Current) (µA)')
    plt.legend()
    slope_text = f"Slope (1/RC) = {params[1]}"
    plt.text(0.002, min(data) + 0.001, slope_text, fontsize=12, color='green')
    plt.grid(True)

    # Show the plot
    plt.show()
