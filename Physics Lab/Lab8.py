import numpy as np

# Given values
angles = np.array([11.01666667, 30.68333333])  # Angles in degrees
angle_error = 0.216667  # Error in degrees
wavelength = 5.8756e-7  # Wavelength in meters

# Convert wavelength to millimeters
wavelength_mm = wavelength * 1e3  # Convert to mm

# Convert angles to radians
average_angle = np.mean(angles)
average_angle_rad = np.radians(average_angle)
angle_error_rad = np.radians(angle_error)

# Calculate lattice constant in mm^-1
lattice_constant = np.sin(average_angle_rad) / wavelength_mm

# Calculate uncertainty in lattice constant
delta_C = (np.cos(average_angle_rad) / wavelength_mm) * angle_error_rad

# Print results
print(f"Lattice constant: {lattice_constant:.2f} mm^-1")
print(f"Uncertainty in lattice constant: {delta_C:.2f} mm^-1")
