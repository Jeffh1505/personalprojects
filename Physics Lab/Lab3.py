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

# Functions to linearize and fit
def linearize(L: list):
    """Linearize the data by applying natural log"""
    return np.log(np.array(L))

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

# Linearize the charging data
charging = [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]
linearized_charging = [linearize(charging_list) for charging_list in charging]

# Linearize the discharging data
discharging = [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]
linearized_discharging = [linearize(discharging_list) for discharging_list in discharging]

# Time in seconds (first 10 points)
time_data = [np.arange(10)] * 3  # Assuming 1 second intervals for each dataset

# Error is 5% of the data values (reduced from 10% to make the bars smaller)
error_charging = [np.array(data) * 0.05 for data in charging]
error_discharging = [np.array(data) * 0.05 for data in discharging]

# Constants
R_load = 510e3  # Load resistance in ohms (510 kΩ)
tolerance = 0.10  # ±10% tolerance
capacitances = [10e-6, 20e-6, 30e-6]  # 10µF, 20µF, 30µF

# Plot and fit each dataset with distinct colors
colors = ['red', 'blue', 'green']  # Use different colors for each plot

# Charging
for i, (time, data, error) in enumerate(zip(time_data, linearized_charging, error_charging)):
    # Perform the curve fitting and get parameters
    params, cov = opt.curve_fit(funclin, time, data, sigma=error, absolute_sigma=True)
    
    # Generate best fit line
    fit_line = funclin(time, *params)

    # Plot the linearized data with error bars and a distinct color for the best fit line
    plt.figure()
    plt.errorbar(time, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Charging)', capsize=3, elinewidth=1, markeredgewidth=1)
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF (Charging)', color=colors[i])

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

# Discharging
for i, (time, data, error) in enumerate(zip(time_data, linearized_discharging, error_discharging)):
    # Perform the curve fitting and get parameters
    params, cov = opt.curve_fit(funclin, time, data, sigma=error, absolute_sigma=True)
    
    # Generate best fit line
    fit_line = funclin(time, *params)

    # Plot the linearized data with error bars and a distinct color for the best fit line
    plt.figure()
    plt.errorbar(time, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Discharging)', capsize=3, elinewidth=1, markeredgewidth=1)
    plt.plot(time, fit_line, label=f'Best Fit {(i+1)*10}µF (Discharging)', color=colors[i])

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
