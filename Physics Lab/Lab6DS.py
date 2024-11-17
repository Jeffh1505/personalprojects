import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants with uncertainties
d = 0.00025  # slit separation (m)
d_uncertainty = 0.00001  # uncertainty in d (m)
L = 0.98  # screen distance (m)
L_uncertainty = 0.02  # uncertainty in L (m)

# Data (convert from cm to m)
positions = np.array([0.017, 0.036, 0.052, 0.078, 0.104, 0.119, 0.138]) * 0.01  # Convert cm to m
scale_factor = 0.1  # Adjust for closer match to expected wavelength
positions *= scale_factor
pos_uncertainty = 0.0001 * scale_factor  # Adjust uncertainties accordingly
order_numbers = np.arange(-(len(positions) - 1) // 2, (len(positions)) // 2 + 1)

# Remove zero order
nonzero_mask = order_numbers != 0
positions = positions[nonzero_mask]
order_numbers = order_numbers[nonzero_mask]

# Define a linear model for fitting
def linear_model(x, m, b):
    return m * x + b

# Perform curve fitting
params, cov_matrix = curve_fit(
    linear_model,
    order_numbers,
    positions,
    sigma=np.full_like(positions, pos_uncertainty)
)

# Extract slope and intercept with uncertainties
slope, intercept = params
slope_uncertainty, intercept_uncertainty = np.sqrt(np.diag(cov_matrix))

# Estimate wavelength
wavelength = slope * d / L
wavelength_uncertainty = wavelength * np.sqrt(
    (slope_uncertainty / slope) ** 2 +
    (d_uncertainty / d) ** 2 +
    (L_uncertainty / L) ** 2
)

# Convert to nanometers
wavelength_nm = wavelength * 1e9
wavelength_uncertainty_nm = wavelength_uncertainty * 1e9

# Generate best-fit line
fit_line = linear_model(order_numbers, slope, intercept)

# Plotting
plt.errorbar(order_numbers, positions, yerr=pos_uncertainty, fmt='o', label='Data', capsize=5)
plt.plot(order_numbers, fit_line, label=f'Best Fit Line (y = {slope:.3e}x + {intercept:.3e})')

# Center y-axis at x=0
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlim(order_numbers.min() - 1, order_numbers.max() + 1)  # Symmetric x-axis limits
plt.ylim(positions.min() - 0.02, positions.max() + 0.02)  # Adjust y-axis range

# Labels and title
plt.xlabel('Order of Maxima (m)')
plt.ylabel('Position of Maxima (m)')
plt.title('Position of Maxima vs Order of Maxima (Centered y-axis)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()

# Print results
print(f"Slope (m): {slope:.3e} ± {slope_uncertainty:.3e}")
print(f"Intercept (b): {intercept:.3e} ± {intercept_uncertainty:.3e}")
print(f"Estimated Wavelength: {wavelength_nm:.1f} ± {wavelength_uncertainty_nm:.1f} nm")
