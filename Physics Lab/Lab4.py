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

def normalize_voltage(voltage):
    return np.array(voltage) / max(voltage)

# Convert regular frequency to angular frequency (ω = 2πf) in rad/s
def to_angular_frequency(frequency):
    return 2 * np.pi * np.array(frequency)

# Convert angular frequency to krad/s for display
def to_krad_per_second(angular_freq):
    return angular_freq / 1000

# Modified interpolation function to work with angular frequencies
def interpolate_data(frequency, voltage, num_points=1000):
    angular_freq = to_angular_frequency(frequency)
    f_interp = interp1d(angular_freq, voltage, kind='cubic')
    angular_freq_interp = np.linspace(min(angular_freq), max(angular_freq), num_points)
    voltage_interp = f_interp(angular_freq_interp)
    return angular_freq_interp, voltage_interp

# Modified resonance finder to work with and return angular frequencies
def find_resonance_and_fwhh(frequency, voltage):
    angular_freq_interp, voltage_interp = interpolate_data(frequency, voltage)
    
    max_voltage = max(voltage_interp)
    half_max_voltage = max_voltage / 2
    
    resonant_index = np.argmax(voltage_interp)
    resonant_angular_freq = angular_freq_interp[resonant_index]
    
    above_half_max = np.where(voltage_interp >= half_max_voltage)[0]
    lower_bound = angular_freq_interp[above_half_max[0]]
    upper_bound = angular_freq_interp[above_half_max[-1]]
    fwhh = upper_bound - lower_bound
    
    freq_step_size = np.mean(np.diff(angular_freq_interp[above_half_max]))
    uncertainty_resonant_freq = freq_step_size / 2
    uncertainty_fwhh = freq_step_size
    
    return resonant_angular_freq, uncertainty_resonant_freq, fwhh, uncertainty_fwhh

# Calculate theoretical angular frequency
inductor_value = 150e-3  # 150 mH
capacitor_value = 0.5e-6  # 0.5 μF
expected_angular_frequency = 1 / np.sqrt(inductor_value * capacitor_value)  # This is already ω = 1/√(LC)

# Normalize voltages
one_point_two_k_voltage_normalized = normalize_voltage(one_point_two_k_voltage)
three_point_three_k_voltage_normalized = normalize_voltage(three_point_three_k_voltage)
four_point_five_k_voltage_normalized = normalize_voltage(four_point_five_k_voltage)

# Calculate resonance for each dataset
one_point_two_k_resonance = find_resonance_and_fwhh(one_point_two_k_frequency, one_point_two_k_voltage_normalized)
three_point_three_k_resonance = find_resonance_and_fwhh(three_point_three_k_frequency, three_point_three_k_voltage_normalized)
four_point_five_k_resonance = find_resonance_and_fwhh(four_point_five_k_frequency, four_point_five_k_voltage_normalized)

# Generate LaTeX table with angular frequencies
def generate_latex_table(resonance_results, expected_freq):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Resonant Angular Frequencies, FWHH, and Expected Angular Frequency with Uncertainties}\n"
    latex_table += "\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
    latex_table += "Dataset & Resonant Frequency (krad/s) & FWHH (krad/s) & Expected Frequency (krad/s) \\\\ \\hline\n"
    
    for i, resonance in enumerate(resonance_results):
        resonant_freq, uncertainty_resonant_freq, fwhh, uncertainty_fwhh = resonance
        # Convert to krad/s for display
        resonant_freq_krad = to_krad_per_second(resonant_freq)
        uncertainty_krad = to_krad_per_second(uncertainty_resonant_freq)
        fwhh_krad = to_krad_per_second(fwhh)
        uncertainty_fwhh_krad = to_krad_per_second(uncertainty_fwhh)
        expected_freq_krad = to_krad_per_second(expected_freq)
        
        latex_table += f"{['1.2 kΩ', '3.3 kΩ', '4.5 kΩ'][i]} & {resonant_freq_krad:.2f} ± {uncertainty_krad:.2f} & {fwhh_krad:.2f} ± {uncertainty_fwhh_krad:.2f} & {expected_freq_krad:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Generate table
resonance_results = [one_point_two_k_resonance, three_point_three_k_resonance, four_point_five_k_resonance]
latex_table_output = generate_latex_table(resonance_results, expected_angular_frequency)

# Print LaTeX table
print(latex_table_output)

# Plotting with angular frequencies
plt.figure(figsize=(10, 6))
datasets = [
    (one_point_two_k_frequency, one_point_two_k_voltage_normalized, "1.2 kΩ"),
    (three_point_three_k_frequency, three_point_three_k_voltage_normalized, "3.3 kΩ"),
    (four_point_five_k_frequency, four_point_five_k_voltage_normalized, "4.5 kΩ")
]

for freq, volt, label in datasets:
    angular_freq_interp, volt_interp = interpolate_data(freq, volt)
    plt.plot(to_krad_per_second(angular_freq_interp), volt_interp, label=label, marker='o')

plt.title('Voltage vs. Angular Frequency for Different Resistances')
plt.xlabel('Angular Frequency (krad/s)')
plt.ylabel('Normalized Voltage')
plt.legend()
plt.grid()
plt.tight_layout()

# Save the plot
plt.savefig('voltage_vs_angular_frequency.png')
plt.show()