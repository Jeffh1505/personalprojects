import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Data (no changes to the input data)
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

# Interpolation function for smoother frequency and voltage data
def interpolate_data(frequency, voltage, num_points=1000):
    f_interp = interp1d(frequency, voltage, kind='cubic')
    frequency_interp = np.linspace(min(frequency), max(frequency), num_points)
    voltage_interp = f_interp(frequency_interp)
    return frequency_interp, voltage_interp

# Convert frequency to angular frequency (ω = 2πf)
def angular_frequency(frequency):
    return 2 * np.pi * np.array(frequency)

# Convert frequency to kHz
def frequency_to_khz(frequency):
    return np.array(frequency) / 1000

# Find resonant frequency (where voltage is max) and FWHH
def find_resonance_and_fwhh(frequency, voltage):
    frequency_interp, voltage_interp = interpolate_data(frequency, voltage)
    
    max_voltage = max(voltage_interp)
    half_max_voltage = max_voltage / 2
    
    # Resonant frequency is where the voltage is maximum
    resonant_index = np.argmax(voltage_interp)
    resonant_frequency = frequency_interp[resonant_index]
    
    # FWHH: find where voltage crosses half max
    above_half_max = np.where(voltage_interp >= half_max_voltage)[0]
    lower_bound = frequency_interp[above_half_max[0]]
    upper_bound = frequency_interp[above_half_max[-1]]
    fwhh = upper_bound - lower_bound
    
    # Estimate uncertainty based on step size near the resonance
    freq_step_size = np.mean(np.diff(frequency_interp[above_half_max]))
    uncertainty_resonant_freq = freq_step_size / 2
    uncertainty_fwhh = freq_step_size
    
    return resonant_frequency, uncertainty_resonant_freq, fwhh, uncertainty_fwhh

# Calculate for each dataset
one_point_two_k_resonance = find_resonance_and_fwhh(one_point_two_k_frequency, one_point_two_k_voltage_normalized)
three_point_three_k_resonance = find_resonance_and_fwhh(three_point_three_k_frequency, three_point_three_k_voltage_normalized)
four_point_five_k_resonance = find_resonance_and_fwhh(four_point_five_k_frequency, four_point_five_k_voltage_normalized)

# Plotting function
def plot_data(frequency_khz, voltage, label, marker):
    plt.plot(frequency_khz, voltage, label=label, marker=marker)

# Plotting
plt.figure(figsize=(10, 6))

# Frequencies in kHz for plotting
one_point_two_k_khz = frequency_to_khz(one_point_two_k_frequency)
three_point_three_k_khz = frequency_to_khz(three_point_three_k_frequency)
four_point_five_k_khz = frequency_to_khz(four_point_five_k_frequency)

# Plot for 1.2 kΩ
plot_data(one_point_two_k_khz, one_point_two_k_voltage_normalized, '1.2 kΩ', 'o')

# Plot for 3.3 kΩ
plot_data(three_point_three_k_khz, three_point_three_k_voltage_normalized, '3.3 kΩ', 's')

# Plot for 4.5 kΩ
plot_data(four_point_five_k_khz, four_point_five_k_voltage_normalized, '4.5 kΩ', '^')

# Labels and title
plt.xlabel('Frequency (kHz)')
plt.ylabel('Normalized Voltage')
plt.title('Normalized Voltage vs Frequency (kHz)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Calculate the expected resonant frequency
L = 150e-3  # 150 mH
C = 0.5e-6  # 0.5 µF
f_expected = 1 / (2 * np.pi * np.sqrt(L * C))

# Display results
datasets = ['1.2 kΩ', '3.3 kΩ', '4.5 kΩ']
results = [one_point_two_k_resonance, three_point_three_k_resonance, four_point_five_k_resonance]

print(f"Expected Resonant Frequency: {f_expected:.2f} Hz\n")
print("Dataset | Resonant Frequency (Hz) ± Uncertainty | FWHH (Hz) ± Uncertainty")
for i, result in enumerate(results):
    print(f"{datasets[i]} | {result[0]:.2f} ± {result[1]:.2f} | {result[2]:.2f} ± {result[3]:.2f}")

# LaTeX Table Output
def generate_latex_table(expected_freq):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Resonant Frequencies, FWHH, and Expected Resonant Frequency with Uncertainties}\n\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
    latex_table += "Dataset & Resonant Frequency (Hz) & FWHH (Hz) & Expected Resonant Frequency (Hz) \\\\ \\hline\n"
    
    for i, result in enumerate(results):
        latex_table += f"{datasets[i]} & {result[0]:.2f} ± {result[1]:.2f} & {result[2]:.2f} ± {result[3]:.2f} & {expected_freq:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Generate the LaTeX table
latex_table_output = generate_latex_table(f_expected)
print("\nLaTeX Table:\n")
print(latex_table_output)

    
   
