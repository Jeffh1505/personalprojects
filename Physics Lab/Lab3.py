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

# Time in seconds (first 10 points)
time_data = np.arange(10)  # Assuming 1 second intervals for each dataset

# Error is 10% of the data values
error_charging = [np.array(data) * 0.10 for data in [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]]
error_discharging = [np.array(data) * 0.10 for data in [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]]

# Constants
R_load = 510e3  # Load resistance in ohms (510 kΩ)
tolerance = 0.10  # ±10% tolerance
capacitances = [10e-6, 20e-6, 30e-6]  # 10µF, 20µF, 30µF

# Linearize the charging and discharging data
charging = [ten_microfarad_charging, twenty_microfarad_charging, thirty_microfarad_charging]
discharging = [ten_microfarad_discharging, twenty_microfarad_discharging, thirty_microfarad_discharging]
linearized_charging = [linearize(charging_list) for charging_list in charging]
linearized_discharging = [linearize(discharging_list) for discharging_list in discharging]

# Store total resistances and internal resistances for charging and discharging
total_resistances_charging = []
internal_resistances_charging = []
total_resistances_discharging = []

# Plot charging data
plt.figure()

for i, (data, error) in enumerate(zip(linearized_charging, error_charging)):
    params, _ = opt.curve_fit(funclin, time_data, data, sigma=error, absolute_sigma=True)
    slope = params[1]  # Slope (1/RC)
    C = capacitances[i]
    R_total = -1 / (slope * C)  # R_total = -1/(slope * C)
    R_total_tolerance = R_total * (1 + tolerance)  # Max total resistance with tolerance
    R_internal = R_total_tolerance - R_load  # R_internal = R_total - R_load
    
    total_resistances_charging.append(R_total)
    internal_resistances_charging.append(R_internal)
    
    fit_line = funclin(time_data, *params)
    
    plt.errorbar(time_data, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Charging)', capsize=3, elinewidth=1, markeredgewidth=1)
    plt.plot(time_data, fit_line, label=f'Best Fit {(i+1)*10}µF (Charging)', color='red')
    
plt.title('Linearized Charging Data with Best Fit')
plt.xlabel('Time (seconds)')
plt.ylabel('ln(Current) (µA)')
plt.legend()
plt.grid(True)
plt.show()

# Plot discharging data
plt.figure()

for i, (data, error) in enumerate(zip(linearized_discharging, error_discharging)):
    params, _ = opt.curve_fit(funclin, time_data, data, sigma=error, absolute_sigma=True)
    slope = params[1]  # Slope (1/RC)
    C = capacitances[i]
    R_total = -1 / (slope * C)  # R_total = -1/(slope * C)
    
    total_resistances_discharging.append(R_total)
    
    fit_line = funclin(time_data, *params)
    
    plt.errorbar(time_data, data, yerr=error, fmt='o', label=f'{(i+1)*10}µF (Discharging)', capsize=3, elinewidth=1, markeredgewidth=1)
    plt.plot(time_data, fit_line, label=f'Best Fit {(i+1)*10}µF (Discharging)', color='red')

plt.title('Linearized Discharging Data with Best Fit')
plt.xlabel('Time (seconds)')
plt.ylabel('ln(Current) (µA)')
plt.legend()
plt.grid(True)
plt.show()
