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

# Function for linearizing data
def linearize(L: list):
    return np.log(np.array(L))

# Linear function for fitting
def funclin(x, a, b):
    return a + b * x

# Colors for distinct capacitances
colors = ['blue', 'green', 'orange']

# Time in seconds (first 10 points)
time_data = np.arange(10)

# Error is 10% of the data values
error_charging = [np.array(data) * 0.10 for data in [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]]
error_discharging = [np.array(data) * 0.10 for data in [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]]

# Time constants and errors storage
time_constants_charging = []
time_constants_discharging = []

# Plot for charging data
plt.figure(figsize=(8, 6))

for i, (charging_data, error, color) in enumerate(zip([ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging], error_charging, colors)):
    linearized_charging = linearize(charging_data)
    params, cov = opt.curve_fit(funclin, time_data, linearized_charging, sigma=error, absolute_sigma=True)
    fit_line = funclin(time_data, *params)
    
    # Extract slope and intercept
    slope = params[1]
    slope_error = np.sqrt(cov[1, 1])
    
    # Compute time constant and its error
    tau = -1 / slope
    tau_error = slope_error / slope**2
    
    # Store the time constant and error
    time_constants_charging.append((tau, tau_error))
    
    # Plot the linearized data with error bars and best fit line
    plt.errorbar(time_data, linearized_charging, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Charging)', color=color, capsize=3)
    plt.plot(time_data, fit_line, label=f'Best Fit {(i+1)*10}µF', color=color, linestyle='--')

# Customize the charging plot
plt.title('Linearized Charging Data with Best Fit Lines')
plt.xlabel('Time (seconds)')
plt.ylabel('ln(Current) (µA)')
plt.legend()
plt.grid(True)
plt.show()

# Plot for discharging data
plt.figure(figsize=(8, 6))

for i, (discharging_data, error, color) in enumerate(zip([ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging], error_discharging, colors)):
    linearized_discharging = linearize(discharging_data)
    params, cov = opt.curve_fit(funclin, time_data, linearized_discharging, sigma=error, absolute_sigma=True)
    fit_line = funclin(time_data, *params)
    
    # Extract slope and intercept
    slope = params[1]
    slope_error = np.sqrt(cov[1, 1])
    
    # Compute time constant and its error
    tau = -1 / slope
    tau_error = slope_error / slope**2
    
    # Store the time constant and error
    time_constants_discharging.append((tau, tau_error))
    
    # Plot the linearized data with error bars and best fit line
    plt.errorbar(time_data, linearized_discharging, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Discharging)', color=color, capsize=3)
    plt.plot(time_data, fit_line, label=f'Best Fit {(i+1)*10}µF', color=color, linestyle='--')

# Customize the discharging plot
plt.title('Linearized Discharging Data with Best Fit Lines')
plt.xlabel('Time (seconds)')
plt.ylabel('ln(Current) (µA)')
plt.legend()
plt.grid(True)
plt.show()

# Report time constants with errors
print("Charging Time Constants (µF):")
for i, (tau, tau_error) in enumerate(time_constants_charging):
    print(f"Capacitance: {(i+1)*10}µF, Time Constant: {tau:.4f} s, Error: ±{tau_error:.4f} s")

print("\nDischarging Time Constants (µF):")
for i, (tau, tau_error) in enumerate(time_constants_discharging):
    print(f"Capacitance: {(i+1)*10}µF, Time Constant: {tau:.4f} s, Error: ±{tau_error:.4f} s")
