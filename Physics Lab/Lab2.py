import math
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the mean and standard deviation
def unweighted_stats(data: list) -> tuple:
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # ddof=1 for sample standard deviation
    std_error = std_dev / np.sqrt(len(data))
    return mean, std_error

# Function to convert a dataset into a LaTeX table format
def to_latex_table(data: list, columns: list, caption: str, label: str) -> str:
    table_str = "\\begin{table}[ht]\n\\centering\n\\begin{tabular}{|" + "c|" * len(columns) + "}\n\\hline\n"
    table_str += " & ".join(columns) + " \\\\ \\hline\n"
    
    for row in zip(*data):
        table_str += " & ".join(f"{item:.2f}" if isinstance(item, (float, int)) else item for item in row) + " \\\\ \\hline\n"
    
    table_str += "\\end{tabular}\n"
    table_str += f"\\caption{{{caption}}}\n"
    table_str += f"\\label{{{label}}}\n"
    table_str += "\\end{table}\n"
    return table_str

# Function to create LaTeX table for unweighted stats
def stats_to_latex_table(stats: dict, caption: str, label: str) -> str:
    table_str = "\\begin{table}[ht]\n\\centering\n\\begin{tabular}{|c|c|c|}\n\\hline\n"
    table_str += "Axis & Mean (cm) & Standard Error (cm) \\\\ \\hline\n"
    
    for axis, (mean, std_err) in stats.items():
        table_str += f"{axis} & {mean:.3f} & {std_err:.3f} \\\\ \\hline\n"
    
    table_str += "\\end{tabular}\n"
    table_str += f"\\caption{{{caption}}}\n"
    table_str += f"\\label{{{label}}}\n"
    table_str += "\\end{table}\n"
    return table_str

# Function to save histograms
def save_histogram(data, title, xlabel, filename, bins=20, color='blue'):
    plt.figure(figsize=(10, 6))  # Set figure size
    plt.hist(data, bins=bins, color=color, alpha=0.7, edgecolor='black', linewidth=1.2)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(axis='y', alpha=0.75)  # Add grid lines for better readability
    
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.tight_layout()  # Adjust layout
    plt.savefig(filename)
    plt.clf()  # Clear the figure for the next plot

# Dataset A (example raw data)
x_distance_a = [68.2, 68.2, 68.2, 68.1, 68.1, 68.1, 68, 67.5, 67.5, 67.3, 67.2, 67.2, 67.1, 67, 66.9, 
                66.8, 66.7, 66.5, 66.5, 66.4, 65.7, 65.8, 65.8, 65.3, 65.2, 65.1, 65, 64, 63.6, 62.8]
x_deviation_a = [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 6.1, 
                 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 9.4, 10.2]
z_deviation_a = [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 0.1, 
                 -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 0.3, 0.4, 0.5, 0.1]

# Dataset B (example raw data)
x_distance_b = [72.2, 72.6, 72.7, 73, 73.3, 73.5, 74, 74.3, 75.6, 73.8, 73.9, 74.5, 75, 75, 75, 
                75.2, 75.1, 75.6, 75.5, 75.6, 75.9, 76.3, 76.4, 76.5, 76.5, 76.7, 76.6, 76.8, 
                76.8, 76.9, 76.9, 77.4, 77.3]
x_deviation_b = [-2.3, 3.8, 1.2, 1.4, -0.6, 1.8, 1.9, 1.9, 0.4, -0.2, -1.2, -1.9, 1.7, 0.8, 
                 0.3, 0.6, 0.1, 1.6, 0.2, -0.4, 0.6, 0.8, -0.6, 0.4, 0.3, 0.5, -0.4, 1.3, 
                 -0.5, 0, -0.5, 0.6, -0.6]
z_deviation_b = [14.7, 14.3, 14.2, 13.9, 13.6, 13.4, 12.9, 12.6, 11.3, 13.1, 13, 12.4, 11.9, 
                 11.9, 11.9, 11.7, 11.8, 11.3, 11.4, 11.3, 11, 10.6, 10.5, 10.4, 10.4, 10.2, 
                 10.3, 10.1, 10.1, 10, 10, 9.5, 9.6]

# Prepare LaTeX tables for datasets A and B
columns = ["x-distance (cm)", "x-deviation (cm)", "z-deviation (cm)"]
data_a = [x_distance_a, x_deviation_a, z_deviation_a]
data_b = [x_distance_b, x_deviation_b, z_deviation_b]

latex_table_a = to_latex_table(data_a, columns, "Raw Data for Dataset A", "tab:dataset_a")
latex_table_b = to_latex_table(data_b, columns, "Raw Data for Dataset B", "tab:dataset_b")

# Calculate unweighted stats for datasets A and B
x_pos_avg_a, x_pos_std_err_a = unweighted_stats(x_distance_a)
x_avg_a, x_std_err_a = unweighted_stats(x_deviation_a)
z_avg_a, z_std_err_a = unweighted_stats(z_deviation_a)
print(f"x = {x_pos_avg_a} ± {x_pos_std_err_a} cm")
print(f"z = {z_avg_a} ± {z_std_err_a} cm")
x_pos_avg_b, x_pos_std_err_b = unweighted_stats(x_distance_b)
x_avg_b, x_std_err_b = unweighted_stats(x_deviation_b)
z_avg_b, z_std_err_b = unweighted_stats(z_deviation_b)
print(f"x = {x_pos_avg_b} ± {x_pos_std_err_b} cm")
print(f"z = {z_avg_b} ± {z_std_err_b} cm")
# Prepare LaTeX tables for unweighted stats
stats_a = {
    'x-axis': (x_avg_a, x_std_err_a),
    'z-axis': (z_avg_a, z_std_err_a)
}
stats_b = {
    'x-axis': (x_avg_b, x_std_err_b),
    'z-axis': (z_avg_b, z_std_err_b)
}

latex_stats_a = stats_to_latex_table(stats_a, "Unweighted Statistics for Dataset A", "tab:stats_a")
latex_stats_b = stats_to_latex_table(stats_b, "Unweighted Statistics for Dataset B", "tab:stats_b")

# Save histograms for both datasets
save_histogram(x_distance_a, "Histogram of x-distance Measurements (Dataset 1)", "x-distance (cm)", "histogram_x_1.png", bins=10, color='blue')
save_histogram(x_distance_b, "Histogram of x-distance Measurements (Dataset 2)", "x-distance (cm)", "histogram_x_2.png", bins=10, color='orange')
save_histogram(z_deviation_a, "Histogram of z-distance Measurements (Dataset 1)", "x-distance (cm)", "histogram_z_1.png", bins=10, color='red')
save_histogram(z_deviation_b, "Histogram of z-distance Measurements (Dataset 2)", "x-distance (cm)", "histogram_z_2.png", bins=10, color='green')
# Output the LaTeX tables
print("LaTeX Table for Dataset A:")
print(latex_table_a)
print("\nLaTeX Table for Unweighted Stats A:")
print(latex_stats_a)

print("\nLaTeX Table for Dataset B:")
print(latex_table_b)
print("\nLaTeX Table for Unweighted Stats B:")
print(latex_stats_b)
