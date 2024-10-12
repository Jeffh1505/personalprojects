import math
import matplotlib.pyplot as plt 
import numpy as np

# Data
x_distance_a = [68.2, 68.2, 68.2, 68.1, 68.1, 68.1, 68, 67.5, 67.5, 67.3, 67.2, 67.2,
                67.1, 67, 66.9, 66.8, 66.7, 66.5, 66.5, 66.4, 65.7, 65.8, 65.8, 65.3, 
                65.2, 65.1, 65, 64, 63.6, 62.8]
x_deviation_a = [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 
                 6.1, 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 
                 9.4, 10.2]
z_deviation_a = [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 
                 0.1, -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 
                 0.3, 0.4, 0.5, 0.1]

# Function to calculate the mean and standard deviation
def unweighted_stats(data: list) -> tuple:
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
    std_error = std_dev / np.sqrt(len(data))
    return mean, std_error

# Calculate the mean and standard deviation for x and z deviations
x_avg, x_std_err = unweighted_stats(x_deviation_a)
z_avg, z_std_err = unweighted_stats(z_deviation_a)

print(f"Motion along x-axis: {x_avg:.3f} cm ± {x_std_err:.3f}")
print(f"Motion along z-axis: {z_avg:.3f} cm ± {z_std_err:.3f}")

# Expected values
x_expected = 72.99  # Adjust as needed
z_expected = 0  # Assuming no motion along z-axis

# Center the data by adjusting the deviation
x_centered = [val - x_avg for val in x_deviation_a]
z_centered = [val - z_avg for val in z_deviation_a]

# Create histograms
plt.figure(figsize=(12, 6))

# Histogram for x-deviation (centered)
plt.subplot(1, 2, 1)
plt.hist(x_centered, bins=10, color='blue', edgecolor='black')
plt.title("Centered Histogram of x-deviation measurements")
plt.xlabel("Deviation from Mean (cm)")
plt.ylabel("Frequency")

# Histogram for z-deviation (centered)
plt.subplot(1, 2, 2)
plt.hist(z_centered, bins=10, color='green', edgecolor='black')
plt.title("Centered Histogram of z-deviation measurements")
plt.xlabel("Deviation from Mean (cm)")
plt.ylabel("Frequency")

# Show the centered histograms
plt.tight_layout()
plt.show()
