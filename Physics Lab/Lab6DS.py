import numpy as np

# Constants with uncertainties
d = 0.00025  # slit separation (m)
d_uncertainty = 0.00001  # uncertainty in d (m)
L = 1.030  # screen distance (m)
L_uncertainty = 0.02  # uncertainty in L (m)

# Data (convert from cm to m)
positions = np.array([0.017, 0.036, 0.052, 0.078, 0.104, 0.119, 0.138]) * 0.01  # Convert cm to m
pos_uncertainty = 0.0001  # 0.1 mm position uncertainty
order_numbers = np.arange(-(len(positions) - 1) // 2, (len(positions)) // 2 + 1)

# Remove zero order
nonzero_mask = order_numbers != 0
positions = positions[nonzero_mask]
order_numbers = order_numbers[nonzero_mask]

# Calculate wavelengths for nominal L
angles = np.arctan(positions / L)
wavelengths = (d * np.sin(angles)) / np.abs(order_numbers)
wavelengths_nm = wavelengths * 1e9

# Calculate wavelengths for L + uncertainty
angles_plus = np.arctan(positions / (L + L_uncertainty))
wavelengths_plus = (d * np.sin(angles_plus)) / np.abs(order_numbers)

# Calculate wavelengths for L - uncertainty
angles_minus = np.arctan(positions / (L - L_uncertainty))
wavelengths_minus = (d * np.sin(angles_minus)) / np.abs(order_numbers)

# Calculate uncertainty due to L
L_contribution = np.abs(wavelengths_plus - wavelengths_minus) / 2

# Total uncertainty (combining L, d, and position uncertainties)
# Using error propagation formula
relative_uncertainty = np.sqrt((L_uncertainty/L)**2 + (d_uncertainty/d)**2 + (pos_uncertainty/positions)**2)
total_uncertainty = np.mean(wavelengths) * relative_uncertainty

# Convert all to nm
mean_wavelength = np.mean(wavelengths_nm)
uncertainty_nm = total_uncertainty * 1e9

print("Detailed calculations for each order:")
print("-" * 60)
print("Order | Position (mm) | Angle (deg) | Wavelength (nm)")
print("-" * 60)
for m, pos, ang, wave in zip(order_numbers, positions, angles, wavelengths_nm):
    print(f"{m:5d} | {pos*1000:11.3f} | {np.degrees(ang):10.3f} | {wave:13.1f}")

print("\nFinal Result:")
print(f"Wavelength = {mean_wavelength:.1f} ± {uncertainty_nm:.1f} nm")

print("\nUncertainty Breakdown:")
print(f"Uncertainty due to L: ±{np.mean(L_contribution)*1e9:.1f} nm")
print(f"Relative uncertainty: {relative_uncertainty*100:.1f}%")

# Compare with common laser wavelengths
print("\nComparison with common lasers:")
common_lasers = {
    "Red HeNe": 632.8,
    "Red Diode": 650.0,
    "Green HeNe": 543.5,
    "Green Diode": 532.0
}

for laser, wave in common_lasers.items():
    diff = abs(wave - mean_wavelength)
    if diff < mean_wavelength * 0.2:  # Only show reasonably close matches
        print(f"{laser} laser ({wave} nm)")
        print(f"Difference from measured: {diff:.1f} nm")
        print(f"Within uncertainty? {'Yes' if diff < uncertainty_nm else 'No'}")

# Calculate effect of adjusting L within its uncertainty
print("\nEffect of adjusting L:")
L_values = [L - L_uncertainty, L, L + L_uncertainty]
for L_test in L_values:
    angles_test = np.arctan(positions / L_test)
    wavelengths_test = (d * np.sin(angles_test)) / np.abs(order_numbers)
    mean_wave_test = np.mean(wavelengths_test) * 1e9
    print(f"L = {L_test*100:.1f} cm: λ = {mean_wave_test:.1f} nm")