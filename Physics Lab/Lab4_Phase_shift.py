import numpy as np

# Data: Frequency in Hz and Time Difference in microseconds
data = [
    (184.2, 320),
    (381, 80),
    (581.3, 40),
    (776.3, 40),
    (981, -40)
]

# Function to calculate phase difference in terms of pi
def calculate_phase_difference_pi(frequency, time_difference_micro):
    # Convert time difference from microseconds to seconds
    time_difference = time_difference_micro * 1e-6
    # Calculate the period of the signal
    period = 1 / frequency
    # Calculate phase difference in radians, then express as a multiple of pi
    phase_difference_radians = (time_difference / period) * 2 * np.pi
    phase_difference_pi = phase_difference_radians / np.pi
    return phase_difference_pi

# Calculate phase differences and store results
results = [(freq, time_diff, calculate_phase_difference_pi(freq, time_diff)) for freq, time_diff in data]

# Generate LaTeX table
def generate_latex_table(results):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Phase Difference Calculations in Terms of $\\pi$}\n"
    latex_table += "\\begin{tabular}{|c|c|c|}\n\\hline\n"
    latex_table += "Frequency (Hz) & Time Difference (µs) & Phase Difference ($\\pi$) \\\\ \\hline\n"
    
    for freq, time_diff, phase_diff_pi in results:
        latex_table += f"{freq:.1f} & {time_diff} & {phase_diff_pi:.2f}$\\pi$ \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Print LaTeX table
latex_table_output = generate_latex_table(results)
print(latex_table_output)
