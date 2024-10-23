import numpy as np
import matplotlib.pyplot as plt

# Data
one_point_two_k_voltage = [3.6, 8.4, 11.4, 13.8, 15.4, 15.8, 16.4, 16.4, 16.6, 16.6, 16.2, 16.2, 16, 15.8, 15.2, 12, 7.28, 4, 2.72, 2.16]
one_point_two_k_frequency = [40.2, 103.5, 160.3, 219, 286, 337.4, 401.9, 463.1, 526.3, 579, 642.6, 704.7, 766.8, 822.3, 1172.3, 2080.7, 4970.2, 10020, 15620, 20700]

three_point_three_k_voltage = [8.8, 16.2, 18.6, 19.4, 20, 20, 20.2, 20.2, 20.2, 20.2, 20, 20, 19.8, 19.8, 19.6, 18.4, 14.8, 10, 7.2, 5.6]
three_point_three_k_frequency = [39.1, 103.3, 160.1, 219.6, 280.2, 341.5, 403.9, 461.2, 521.9, 580.9, 641.8, 692.6, 761, 816.6, 1027.6, 2123, 5111.6, 10080, 15430, 20490]

four_point_five_k_voltage = [11.2, 18.2, 19.8, 20.6, 20.6, 20.8, 20.8, 20.8, 20.8, 20.8, 20.6, 20.6, 20.6, 20.6, 20.2, 19.4, 17, 12.2, 9.6, 7.4]
four_point_five_k_frequency = [38.7, 101.5, 159.9, 223.3, 278.6, 342.4, 398, 455.5, 523.9, 582.3, 643.1, 695.3, 761.2, 821, 1012.3, 2051.1, 5008.1, 10360, 15270, 20570]

# Normalize voltage
def normalize_voltage(voltage):
    return np.array(voltage) / max(voltage)

one_point_two_k_voltage_normalized = normalize_voltage(one_point_two_k_voltage)
three_point_three_k_voltage_normalized = normalize_voltage(three_point_three_k_voltage)
four_point_five_k_voltage_normalized = normalize_voltage(four_point_five_k_voltage)

# Convert frequency to angular frequency (ω = 2πf)
def angular_frequency(frequency):
    return 2 * np.pi * np.array(frequency)

# Find resonant frequency (where voltage is max) and FWHH
def find_resonance_and_fwhh(frequency, voltage):
    max_voltage = max(voltage)
    half_max_voltage = max_voltage / 2
    
    # Resonant frequency is where the voltage is maximum
    resonant_index = np.argmax(voltage)
    resonant_frequency = frequency[resonant_index]
    
    # FWHH: find where voltage crosses half max
    above_half_max = np.where(voltage >= half_max_voltage)[0]
    lower_bound = frequency[above_half_max[0]]
    upper_bound = frequency[above_half_max[-1]]
    fwhh = upper_bound - lower_bound
    
    # Estimate uncertainty based on step size
    freq_step_size = np.mean(np.diff(frequency))
    uncertainty_resonant_freq = freq_step_size / 2
    uncertainty_fwhh = freq_step_size
    
    return resonant_frequency, uncertainty_resonant_freq, fwhh, uncertainty_fwhh

# Calculate for each dataset
one_point_two_k_resonance = find_resonance_and_fwhh(one_point_two_k_frequency, one_point_two_k_voltage_normalized)
three_point_three_k_resonance = find_resonance_and_fwhh(three_point_three_k_frequency, three_point_three_k_voltage_normalized)
four_point_five_k_resonance = find_resonance_and_fwhh(four_point_five_k_frequency, four_point_five_k_voltage_normalized)

# Plotting function
def plot_data(angular_freq, voltage, label, marker):
    plt.plot(angular_freq, voltage, label=label, marker=marker)

# Plotting
plt.figure(figsize=(10, 6))

# Angular frequencies for plotting
one_point_two_k_omega = angular_frequency(one_point_two_k_frequency)
three_point_three_k_omega = angular_frequency(three_point_three_k_frequency)
four_point_five_k_omega = angular_frequency(four_point_five_k_frequency)

# Plot for 1.2 kΩ
plot_data(one_point_two_k_omega, one_point_two_k_voltage_normalized, '1.2 kΩ', 'o')

# Plot for 3.3 kΩ
plot_data(three_point_three_k_omega, three_point_three_k_voltage_normalized, '3.3 kΩ', 's')

# Plot for 4.5 kΩ
plot_data(four_point_five_k_omega, four_point_five_k_voltage_normalized, '4.5 kΩ', '^')

# Labels and title
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Normalized Voltage')
plt.title('Normalized Voltage vs Angular Frequency')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Display results
datasets = ['1.2 kΩ', '3.3 kΩ', '4.5 kΩ']
results = [one_point_two_k_resonance, three_point_three_k_resonance, four_point_five_k_resonance]

print("Dataset | Resonant Frequency (Hz) ± Uncertainty | FWHH (Hz) ± Uncertainty")
for i, result in enumerate(results):
    print(f"{datasets[i]} | {result[0]:.2f} ± {result[1]:.2f} | {result[2]:.2f} ± {result[3]:.2f}")

# LaTeX Table Output
def generate_latex_table():
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Resonant Frequencies and FWHH with Uncertainties}\n\\begin{tabular}{|c|c|c|}\n\\hline\n"
    latex_table += "Dataset & Resonant Frequency (Hz) & FWHH (Hz) \\\\ \\hline\n"
    
    for i, result in enumerate(results):
        latex_table += f"{datasets[i]} & {result[0]:.2f} ± {result[1]:.2f} & {result[2]:.2f} ± {result[3]:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    
    return latex_table

# Output the LaTeX table
latex_table = generate_latex_table()
print("\nLaTeX Table:")
print(latex_table)
