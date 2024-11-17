import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Data: angles (degrees) and intensities
angles = np.array([2.3, 5.9, 12.7, 24.9, 40.9, 59, 79.2, 89.8, 99.6, 111.3, 
                   124.3, 136.1, 150, 169.4, 181.7, 204.7, 225.4, 236.6, 265, 
                   279.9, 294.5, 307.5, 328.2, 351.7, 360])
intensities = np.array([625.19, 1105.35, 1461.13, 2091.75, 2723.31, 3010.59, 
                        2678.94, 2238.71, 1767, 1170.12, 581.31, 194.83, 23.09, 
                        383.12, 903.23, 2095.11, 2894.86, 3048.86, 2466.2, 
                        1768.76, 1014, 447.6, 24.29, 470.51, 837.93])

# Step 1: Find I_0 (maximum intensity) and its associated angle
I_0 = np.max(intensities)
max_angle = angles[np.argmax(intensities)]

# Step 2: Calculate adjusted angles (angles - max_angle) in degrees
adjusted_angles = angles - max_angle

# Step 3: Calculate cos^2 of adjusted angles (in degrees)
cos_squared = np.cos(np.deg2rad(adjusted_angles)) ** 2

# Step 4: Calculate I/I_0
normalized_intensity = intensities / I_0

# Step 5: Downsample to 20 points for clarity in the plot
indices = np.linspace(0, len(angles) - 1, 20, dtype=int)
cos_squared_sampled = cos_squared[indices]
normalized_intensity_sampled = normalized_intensity[indices]

# Step 6: Calculate x-error for cos^2(theta) due to ±0.1 degrees uncertainty
angle_error_deg = 0.1
angle_error_cos_squared = np.abs(np.cos(np.deg2rad(adjusted_angles + angle_error_deg)) ** 2 - cos_squared)

# Sample down the x-errors for the plot
cos_squared_sampled_error = angle_error_cos_squared[indices]

# Step 7: Define y-error for normalized intensity due to ±1 intensity uncertainty
intensity_error = 1 / I_0  # Normalized intensity error

# Step 8: Perform linear regression on the sampled data
slope, intercept, r_value, p_value, std_err = linregress(cos_squared_sampled, normalized_intensity_sampled)

# Step 9: Define the linear fit line
fit_line = slope * cos_squared_sampled + intercept

# Plot the data with error bars and linear fit
plt.figure(figsize=(8, 6))
plt.errorbar(cos_squared_sampled, normalized_intensity_sampled, 
             yerr=intensity_error, xerr=cos_squared_sampled_error,
             fmt='go', ecolor='gray', capsize=3, label=r'$(I_i, \theta_i)$')
plt.plot(cos_squared_sampled, fit_line, 'b--', label=f'Linear Fit: y = {slope:.3f}x + {intercept:.3f}')

# Plot settings
plt.xlabel(r'$\cos^2(\theta)$')
plt.ylabel(r'$I/I_0$')
plt.title(r'Normalized Intensity vs $\cos^2(\theta)$ with Uncertainties and Linear Fit')
plt.legend()
plt.grid(True)
plt.show()

# Print fit parameters and R-squared value
print(f"Slope: {slope:.3f}")
print(f"Intercept: {intercept:.3f}")
print(f"R-squared: {r_value**2:.3f}")

# Signal-to-noise ratio calculation
signal = I_0

# Find the intensity when the angle is 90 degrees from the maximum intensity angle
angle_90_deg = max_angle + 90
if angle_90_deg > 360:
    angle_90_deg -= 360  # Adjust if angle exceeds 360 degrees

# Find the closest angle to 90 degrees from max_angle
noise_angle_index = np.argmin(np.abs(angles - angle_90_deg))
noise = intensities[noise_angle_index]

# Calculate SNR
snr = signal / noise
print(f"Signal-to-Noise Ratio (SNR): {snr:.3f}")

# LaTeX table output
table_rows = []
for adjusted_angles, intensity in zip(adjusted_angles, intensities):
    table_rows.append(f"{adjusted_angles:.1f} & {intensity:.2f} \\\\")

# Create the LaTeX table
latex_table = r"""
\begin{table}[h!]
\centering
\begin{tabular}{|c|c|}
\hline
Angle (degrees) & Intensity \\
\hline
""" + "\n".join(table_rows) + r"""
\hline
\end{tabular}
\caption{Angle and Intensity Data}
\label{tab:angle_intensity}
\end{table}
"""

print("Copy the following LaTeX table code into your document:")
print(latex_table)
