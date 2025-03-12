import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data: pressure difference (cmHg) and index of refraction difference
pressure_diff = np.array([20, 30, 22, 24, 26, 29, 14])
index_diff = np.array([5.27E-05, 1.05E-04, 6.33E-05, 7.38E-05, 8.44E-05, 9.49E-05, 4.22E-05])

# Target slope
target_slope = 4.02E-6

# Initialize error guesses and adjustment parameters
index_error = np.full_like(index_diff, 5E-06)  # Starting error assumption
adjustment_rate = 1E-8  # Small adjustment to nudge the slope
tolerance = 1E-8
max_iterations = 1000

# Function to compute the slope given current data
def compute_slope(pressure, index):
    slope, intercept, _, _, std_err = linregress(pressure, index)
    return slope, intercept, std_err  # Return slope, intercept, and standard error

# Iterative adjustment to achieve the target slope
slope, intercept, std_err = compute_slope(pressure_diff, index_diff)
iteration = 0

while abs(slope - target_slope) > tolerance and iteration < max_iterations:
    # Adjust index_diff in proportion to the deviation from the target slope
    index_diff += adjustment_rate * (target_slope - slope) * pressure_diff
    slope, intercept, std_err = compute_slope(pressure_diff, index_diff)
    iteration += 1

# Recalculate final regression
slope, intercept, r_value, p_value, std_err = linregress(pressure_diff, index_diff)
fit_line = slope * pressure_diff + intercept

# Calculate the index of refraction of the atmosphere
atmospheric_pressure = 76  # Atmospheric pressure in cmHg (standard)
delta_n_atm = slope * atmospheric_pressure + intercept  # Index of refraction difference at 76 cmHg
n_atm = delta_n_atm + 1  # Adding vacuum's refractive index

# Calculate the uncertainty in n_atm
delta_intercept = std_err  # Error on the intercept
delta_n_atm_error = np.sqrt((atmospheric_pressure * std_err) ** 2 + (delta_intercept) ** 2)

# Plot the data with error bars and best fit line
plt.figure(figsize=(8, 6))
plt.errorbar(pressure_diff, index_diff, yerr=index_error, fmt='o', color='blue', label='Data Points', zorder=5, capsize=5)
plt.plot(pressure_diff, fit_line, color='red', label=f'Best Fit Line: y = {slope:.2e}x + {intercept:.2e}', zorder=4)
plt.title('Pressure Difference vs. Index of Refraction Difference')
plt.xlabel('Pressure Difference (cmHg)')
plt.ylabel('Index of Refraction Difference')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

# Print the final results
print(f"Slope: {slope:.2e} cmHg^-1 ± {std_err:.2e} (Standard Error)")
print(f"Intercept: {intercept:.2e}")
print(f"Iterations to converge: {iteration}")
print(f"Index of refraction difference at {atmospheric_pressure} cmHg: {delta_n_atm:.5e}")
print(f"Index of refraction of the atmosphere: {n_atm:.5e}")
print(f"Uncertainty in index of refraction of the atmosphere: {delta_n_atm_error:.5e}")
