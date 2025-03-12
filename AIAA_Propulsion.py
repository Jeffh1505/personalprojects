import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

# Generate throttle points at every 10%
throttle = np.linspace(0, 100, 11)

# Define the known data points 
throttle_known = [50, 100]
thrust_known = [7.74, 13.01]

# Create a non-linear thrust curve that passes through our known points
# Assuming thrust is 0 at 0% throttle as a physical constraint
thrust_data = np.zeros_like(throttle)
thrust_data[0] = 0  # 0% throttle = 0 thrust
thrust_data[5] = 7.74  # 50% throttle = 7.74 lbf
thrust_data[10] = 13.01  # 100% throttle = 13.01 lbf

# For the remaining points, use a smooth curve shape
# We'll use PCHIP interpolation to maintain monotonicity
key_points = np.array([0, 50, 100])
key_values = np.array([0, 7.74, 13.01])
interpolator = PchipInterpolator(key_points, key_values)

# Generate the thrust values
for i, t in enumerate(throttle):
    if t not in [0, 50, 100]:
        thrust_data[i] = interpolator(t)

# Create fine-grained points for the smooth curve
throttle_fine = np.linspace(0, 100, 100)
thrust_interpolated = interpolator(throttle_fine)

# Plotting
plt.figure(figsize=(10, 6))

# Main curve with interpolated points
plt.plot(throttle_fine, thrust_interpolated, 'b-', linewidth=2)

# Data points at 10% throttle increments
plt.plot(throttle, thrust_data, 'bo', markersize=8, label='Data points (10% increments)')

# Highlight the known data points
plt.plot(throttle_known, thrust_known, 'bo', markersize=8)

# Labels and Title
plt.xlabel('Throttle (%)', fontsize=12)
plt.ylabel('Thrust (lbf)', fontsize=12)
plt.title('Throttle vs Thrust Relationship', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate the known points
for x, y in zip(throttle_known, thrust_known):
    plt.annotate(f'({x}%, {y} lbf)', 
                xy=(x, y),
                xytext=(x+5, y-0.5),
                fontsize=10,
                arrowprops=dict(arrowstyle='->', color='black', lw=1))

# Set axis limits
plt.xlim(0, 100)
plt.ylim(0, 14)

plt.tight_layout()
plt.show()