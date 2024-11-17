import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Data
positions = np.array([0.017, 0.036, 0.052, 0.078, 0.104, 0.119, 0.138]) * 1000  # Convert to mm
maxima_positions = positions  # All positions are maxima

# Assign order numbers (symmetric about zero)
order_numbers = np.arange(-(len(maxima_positions) - 1) // 2, 
                          (len(maxima_positions)) // 2 + 1)

# Perform linear regression (already uses least squares method)
slope, intercept, r_value, p_value, slope_std_err = linregress(order_numbers, positions)
fit_positions = slope * order_numbers + intercept

# Create extended range for fit line
order_numbers_extended = np.linspace(min(order_numbers), max(order_numbers), 100)
fit_positions_extended = slope * order_numbers_extended + intercept

# Corrected for large angles
L = 1030  # Distance from slits to screen (mm)
d = 0.25  # Slit separation (mm)

# Exclude order 0 explicitly for wavelength calculation
nonzero_order_numbers = order_numbers[order_numbers != 0]
nonzero_maxima_positions = maxima_positions[order_numbers != 0]

# Ensure there are no zeros in nonzero_order_numbers
if any(nonzero_order_numbers == 0):
    raise ValueError("Nonzero order numbers contain zero, which will cause infinite wavelength.")

# Calculate angles and wavelengths
angles = np.arctan(nonzero_maxima_positions / L)
wavelengths = d * np.sin(angles) / np.abs(nonzero_order_numbers)  # Calculate wavelengths
mean_wavelength = np.mean(wavelengths) * 10**6  # Convert to nanometers
std_wavelength = np.std(wavelengths) * 10**6  # Convert to nanometers

# Error propagation for wavelength
L_uncertainty = 1  # mm
d_uncertainty = 0.01  # mm
relative_error = np.sqrt((slope_std_err / slope)**2 + (d_uncertainty / d)**2 + (L_uncertainty / L)**2)
wavelength_uncertainty = mean_wavelength * relative_error

# Create figure with specific size and DPI
plt.figure(figsize=(8, 6), dpi=100)

# Plot data points with error bars (error = ±0.01)
plt.errorbar(order_numbers, maxima_positions, yerr=0.01, fmt='o', color='blue', 
             capsize=3, capthick=1, ecolor='blue', markersize=5, label='Data')

# Plot the linear fit with solid line
plt.plot(order_numbers_extended, fit_positions_extended, '-', color='red', linewidth=1, label='Linear Fit')

# Add the fit equation in a box
equation_text = f'y = {slope:.4f}x + {intercept:.4f}\nR² = {r_value**2:.4f}'
plt.text(0.6, 0.1, equation_text, transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', edgecolor='black', pad=5))

# Set axis labels and title
plt.xlabel('Order number $m$')
plt.ylabel('$x_m$ (mm)')
plt.title('Locations of Double Slit Interference Maxima')

# Set axis ranges similar to the reference image
plt.xlim(-5, 5)
ymax = max(maxima_positions) * 1.1  # Add 10% padding
plt.ylim(0, ymax)

# Move y-axis to x=0
ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

# Print debugging information
print("\nDebugging Outputs:")
print("-" * 40)
print(f"Maxima positions: {maxima_positions}")
print(f"Order numbers: {order_numbers}")
print(f"Slope: {slope:.4f} mm/order")
print(f"Intercept: {intercept:.4f} mm")
print(f"L: {L} mm, d: {d} mm")
print(f"Calculated angles (rad): {angles}")

# Print the least squares fit results
print("\nLeast Squares Fit Results:")
print(f"Slope: {slope:.4f} ± {slope_std_err:.4f} mm/order")
print(f"R-squared: {r_value**2:.4f}")

# Print wavelength calculation results
print("\nWavelength Calculation Results:")
print("-" * 40)
print(f"Mean Wavelength: {mean_wavelength:.1f} ± {wavelength_uncertainty:.1f} nm")
print(f"Standard Deviation of Wavelength: {std_wavelength:.1f} nm")

# Compare with common laser wavelengths
common_lasers = {
    "Red HeNe": 632.8,
    "Green HeNe": 543.5,
    "Blue-Green Argon": 488.0,
    "Red Diode": 650.0,
    "Green Diode": 532.0
}

print("\nComparison with common laser wavelengths:")
print("-" * 40)
for laser, wave in common_lasers.items():
    diff = abs(wave - mean_wavelength)
    if diff < 50:  # Only show reasonably close matches
        print(f"{laser} laser ({wave} nm): Difference = {diff:.1f} nm")
