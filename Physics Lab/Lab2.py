import math
import matplotlib.pyplot as plt 
import numpy as np

# Data
x_distance_a = [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 9.4, 10.2]
z_distance_a = [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 0.1, -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 0.3, 0.4, 0.5, 0.1]

# Function to calculate the average (mean) value
def unweighted_stats(a1:list) -> tuple:
    unweighted_average = sum(a1)/ len(a1)
    sum_for_sigma = sum((x - unweighted_average)**2 for x in a1)
    sigma = math.sqrt(sum_for_sigma / (len(a1) - 1))
    sigma_average = sigma / math.sqrt(len(a1))
    return unweighted_average, sigma_average

# Calculate the average for x and z distance
x_average, x_std = unweighted_stats(x_distance_a)
z_average, z_std = unweighted_stats(z_distance_a)

print(f"Motion along x-axis: {x_average:.3f} cm +- {x_std:.3f}")
print(f"Motion along z-axis: {z_average:.3f} cm +- {z_std:.3f}")

# Expected values
x_expected = 72.99  # You can adjust this value as needed
z_expected = 0  # Assuming 0 as the expected value for z-motion

# Center the data by subtracting the average distance from the expected value
x_centered = [x_expected - (val - x_average) for val in x_distance_a]
z_centered = [z_expected - (val - z_average) for val in z_distance_a]

# Create histograms
plt.figure(figsize=(12, 6))

# Histogram for x-distance (centered)
plt.subplot(1, 2, 1)
plt.hist(x_centered, bins=10, color='blue', edgecolor='black')
plt.title("Centered Histogram of x-distance measurements")
plt.xlabel("Distance (cm)")
plt.ylabel("Frequency")

# Histogram for z-distance (centered)
plt.subplot(1, 2, 2)
plt.hist(z_centered, bins=10, color='green', edgecolor='black')
plt.title("Centered Histogram of z-distance measurements")
plt.xlabel("Distance (cm)")
plt.ylabel("Frequency")

# Show the centered histograms
plt.tight_layout()
plt.show()
