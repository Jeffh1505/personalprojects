import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Data remains unchanged
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

# Convert frequency to angular frequency (ω = 2πf) in kHz
def angular_frequency_khz(frequency):
    angular_freq = 2 * np.pi * np.array(frequency)
    return angular_freq / 1000  # Convert to kHz (kilo radians per second)

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

# Calculate angular frequencies for LaTeX table
def calculate_angular_frequencies(frequencies):
    return angular_frequency_khz(frequencies)

# Calculate angular frequencies for each data set
angular_freq_one_point_two_k = calculate_angular_frequencies(one_point_two_k_frequency)
angular_freq_three_point_three_k = calculate_angular_frequencies(three_point_three_k_frequency)
angular_freq_four_point_five_k = calculate_angular_frequencies(four_point_five_k_frequency)

# Generate the LaTeX table with angular frequencies in kHz
def generate_latex_table_with_angular_freq(resonance_results, angular_freq_results, expected_frequency):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Resonant Frequencies, FWHH, and Expected Resonant Frequency with Uncertainties}\n"
    latex_table += "\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
    latex_table += "Dataset & Resonant Frequency (kHz) & FWHH (kHz) & Expected Resonant Frequency (kHz) \\\\ \\hline\n"
    
    for i, (resonance, angular_freq) in enumerate(zip(resonance_results, angular_freq_results)):
        resonant_freq, uncertainty_resonant_freq, fwhh, uncertainty_fwhh = resonance
        expected_freq_khz = expected_frequency[i]  # Expected frequency in kHz
        
        # Find the index of the closest angular frequency
        closest_index = (np.abs(angular_freq - resonant_freq)).argmin()
        angular_freq_value = angular_freq[closest_index]
        
        latex_table += f"{['1.2 kΩ', '3.3 kΩ', '4.5 kΩ'][i]} & {angular_freq_value:.2f} ± {uncertainty_resonant_freq * 2 * np.pi / 1000:.2f} & {fwhh:.2f} ± {uncertainty_fwhh * 2 * np.pi / 1000:.2f} & {expected_freq_khz:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Expected resonant frequencies based on LC circuit theory
inductor_value = 150e-3  # 150 mH
capacitor_value = 0.5e-6  # 0.5 μF
expected_frequencies = [
    1 / (2 * np.pi * np.sqrt(inductor_value * capacitor_value)),  # for 1.2 kΩ
    1 / (2 * np.pi * np.sqrt(inductor_value * capacitor_value)),  # for 3.3 kΩ
    1 / (2 * np.pi * np.sqrt(inductor_value * capacitor_value)),  # for 4.5 kΩ
]

# Convert expected frequencies to kHz
expected_frequencies_khz = np.array(expected_frequencies) / 1000  # Convert to kHz

# Gather results for LaTeX table generation
resonance_results = [one_point_two_k_resonance, three_point_three_k_resonance, four_point_five_k_resonance]
angular_freq_results = [angular_freq_one_point_two_k, angular_freq_three_point_three_k, angular_freq_four_point_five_k]

# Generate the LaTeX table
latex_table_output = generate_latex_table_with_angular_freq(resonance_results, angular_freq_results, expected_frequencies_khz)

# Print LaTeX table output
print(latex_table_output)

# Plotting the data
plt.figure(figsize=(10, 6))
freqs = [one_point_two_k_frequency, three_point_three_k_frequency, four_point_five_k_frequency]
norm_voltages = [one_point_two_k_voltage_normalized, three_point_three_k_voltage_normalized, four_point_five_k_voltage_normalized]

for i in range(3):
    freq_interp, volt_interp = interpolate_data(freqs[i], norm_voltages[i])
    plt.plot(freq_interp / 1000, volt_interp, label=f'{["1.2 kΩ", "3.3 kΩ", "4.5 kΩ"][i]}', marker='o')  # Divide frequency by 1000 for kHz

plt.title('Voltage vs. Frequency for Different Resistances')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Normalized Voltage')
plt.legend()
plt.grid()
plt.tight_layout()

# Save the plot
plt.savefig('voltage_vs_frequency.png')
plt.show()
