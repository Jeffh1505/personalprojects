import numpy as np

# Constants (all in meters)
d = 0.00025  # slit separation (m)
L = 1.030    # screen distance (m)

# Data (convert from mm to m)
positions = np.array([0.017, 0.036, 0.052, 0.078, 0.104, 0.119, 0.138]) * 0.001  # Convert to meters
order_numbers = np.arange(-(len(positions) - 1) // 2, (len(positions)) // 2 + 1)

# Remove zero order
nonzero_mask = order_numbers != 0
positions = positions[nonzero_mask]
order_numbers = order_numbers[nonzero_mask]

# Calculate wavelength for each position
wavelengths = (d * positions) / (np.abs(order_numbers) * L)

# Convert to nanometers
wavelengths_nm = wavelengths * 1e9

print("Individual wavelength calculations:")
for m, x, wavelength in zip(order_numbers, positions, wavelengths_nm):
    print(f"Order {m}: position = {x*1000:.3f} mm, wavelength = {wavelength:.1f} nm")

print("\nSummary:")
print(f"Mean wavelength: {np.mean(wavelengths_nm):.1f} nm")
print(f"Standard deviation: {np.std(wavelengths_nm):.1f} nm")