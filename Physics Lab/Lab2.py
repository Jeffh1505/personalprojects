import math
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the mean and standard deviation
def unweighted_stats(data: list) -> tuple:
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
    std_error = std_dev / np.sqrt(len(data))
    return mean, std_error

# Generalized function for analyzing data and saving histograms for multiple datasets
def analyze_and_save_datasets(datasets: dict):
    for name, data in datasets.items():
        x_data, x_deviation, z_deviation, x_expected, z_expected = data

        # Calculate the mean and standard deviation for x and z deviations
        x_avg, x_std_err = unweighted_stats(x_deviation)
        z_avg, z_std_err = unweighted_stats(z_deviation)

        print(f"Dataset: {name}")
        print(f"Motion along x-axis: {x_avg:.3f} cm ± {x_std_err:.3f}")
        print(f"Motion along z-axis: {z_avg:.3f} cm ± {z_std_err:.3f}")

        # Center the data by adjusting the deviation
        x_centered = [val - x_avg for val in x_deviation]
        z_centered = [val - z_avg for val in z_deviation]

        # Create and save x-deviation histogram
        plt.figure()
        plt.hist(x_centered, bins=10, color='blue', edgecolor='black')
        plt.title(f"Centered Histogram of x-deviation for {name}")
        plt.xlabel("Deviation from Mean (cm)")
        plt.ylabel("Frequency")
        plt.savefig(f"{name}_x_deviation_histogram.png")  # Save as PNG file
        plt.close()  # Close the figure to prevent overlap

        # Create and save z-deviation histogram
        plt.figure()
        plt.hist(z_centered, bins=10, color='green', edgecolor='black')
        plt.title(f"Centered Histogram of z-deviation for {name}")
        plt.xlabel("Deviation from Mean (cm)")
        plt.ylabel("Frequency")
        plt.savefig(f"{name}_z_deviation_histogram.png")  # Save as PNG file
        plt.close()  # Close the figure to prevent overlap

        print(f"Histograms for {name} saved as '{name}_x_deviation_histogram.png' and '{name}_z_deviation_histogram.png'.\n")

# Dataset (a dataset and b dataset)
datasets = {
    "Dataset_A": ([68.2, 68.2, 68.2, 68.1, 68.1, 68.1, 68, 67.5, 67.5, 67.3, 67.2, 67.2, 67.1, 67, 66.9, 66.8, 66.7, 66.5, 66.5, 66.4, 65.7, 65.8, 65.8, 65.3, 65.2, 65.1, 65, 64, 63.6, 62.8], 
                  [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 9.4, 10.2],
                  [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 0.1, -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 0.3, 0.4, 0.5, 0.1], 
                  72.99, 0),
    "Dataset_B": ([72.2, 72.6, 72.7, 73, 73.3, 73.5, 74, 74.3, 75.6, 73.8, 73.9, 74.5, 75, 75, 
                   75, 75.2, 75.1, 75.6, 75.5, 75.6, 75.9, 76.3, 76.4, 76.5, 76.5, 76.7, 76.6, 
                   76.8, 76.8, 76.9, 76.9, 77.4, 77.3],
                  [-2.3, 3.8, 1.2, 1.4, -0.6, 1.8, 1.9, 1.9, 0.4, -0.2, -1.2, -1.9, 1.7, 0.8, 
                   0.3, 0.6, 0.1, 1.6, 0.2, -0.4, 0.6, 0.8, -0.6, 0.4, 0.3, 0.5, -0.4, 1.3, 
                   -0.5, 0, -0.5, 0.6, -0.6],
                  [14.7, 14.3, 14.2, 13.9, 13.6, 13.4, 12.9, 12.6, 11.3, 13.1, 13, 12.4, 11.9, 
                   11.9, 11.9, 11.7, 11.8, 11.3, 11.4, 11.3, 11, 10.6, 10.5, 10.4, 10.4, 10.2, 
                   10.3, 10.1, 10.1, 10, 10, 9.5, 9.6], 
                  75, 12)
}

# Analyze and save the data for both datasets
analyze_and_save_datasets(datasets)
