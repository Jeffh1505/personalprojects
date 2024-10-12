import math
import matplotlib.pyplot as plt 
import numpy as np

# Function to calculate the mean and standard deviation
def unweighted_stats(data: list) -> tuple:
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
    std_error = std_dev / np.sqrt(len(data))
    return mean, std_error

# Generalized function for analyzing data
def analyze_motion_data(x_data: list, x_deviation: list, z_deviation: list, x_expected: float = 72.99, z_expected: float = 0):
    # Calculate the mean and standard deviation for x and z deviations
    x_avg, x_std_err = unweighted_stats(x_deviation)
    z_avg, z_std_err = unweighted_stats(z_deviation)

    print(f"Motion along x-axis: {x_avg:.3f} cm ± {x_std_err:.3f}")
    print(f"Motion along z-axis: {z_avg:.3f} cm ± {z_std_err:.3f}")

    # Center the data by adjusting the deviation
    x_centered = [val - x_avg for val in x_deviation]
    z_centered = [val - z_avg for val in z_deviation]

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

# Sample dataset (x-distance and deviations)
x_distance_a = [68.2, 68.2, 68.2, 68.1, 68.1, 68.1, 68, 67.5, 67.5, 67.3, 67.2, 67.2,
                67.1, 67, 66.9, 66.8, 66.7, 66.5, 66.5, 66.4, 65.7, 65.8, 65.8, 65.3, 
                65.2, 65.1, 65, 64, 63.6, 62.8]
x_deviation_a = [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 
                 6.1, 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 
                 9.4, 10.2]
z_deviation_a = [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 
                 0.1, -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 
                 0.3, 0.4, 0.5, 0.1]

# Analyze the sample data
analyze_motion_data(x_distance_a, x_deviation_a, z_deviation_a)

# If you have another dataset, just call the function with the new data
# Example:
x_distance_b = [70.1, 70.2, 70.3, 69.9, 69.8, 69.7]  # Replace with your data
x_deviation_b = [4.5, 4.6, 4.7, 5, 4.8, 5.1]        # Replace with your data
z_deviation_b = [0, -0.1, 0.2, 0.1, -0.2, 0.3]      # Replace with your data

analyze_motion_data(x_distance_b, x_deviation_b, z_deviation_b, x_expected=70.5, z_expected=0)
