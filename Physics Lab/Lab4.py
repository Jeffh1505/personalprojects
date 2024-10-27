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

# Convert regular frequency to angular frequency (ω = 2πf)
def to_angular_frequency(frequency):
    return 2 * np.pi * np.array(frequency)

# Convert angular frequency to kHz (ω/1000)
def to_angular_khz(angular_freq):
    return angular_freq / 1000

# Modified interpolation function to work with angular frequencies
def interpolate_data(frequency, voltage, num_points=1000):
    angular_freq = to_angular_frequency(frequency)
    f_interp = interp1d(angular_freq, voltage, kind='cubic')
    angular_freq_interp = np.linspace(min(angular_freq), max(angular_freq), num_points)
    voltage_interp = f_interp(angular_freq_interp)
    return angular_freq_interp, voltage_interp

# Modified resonance finder to work with angular frequencies
def find_resonance_and_fwhh(frequency, voltage):
    angular_freq = to_angular_frequency(frequency)
    
    # Find resonant frequency directly from raw data
    resonant_index = np.argmax(voltage)
    resonant_angular_freq = angular_freq[resonant_index]
    
    # Calculate FWHH directly from raw data
    max_voltage = max(voltage)
    half_max_voltage = max_voltage / 2
    
    above_half_max = np.where(voltage >= half_max_voltage)[0]
    lower_bound = angular_freq[above_half_max[0]]
    upper_bound = angular_freq[above_half_max[-1]]
    fwhh = upper_bound - lower_bound
    
    # Estimate uncertainties based on frequency step size
    freq_step_size = np.mean(np.diff(angular_freq[above_half_max]))
    uncertainty_resonant_freq = freq_step_size / 2
    uncertainty_fwhh = freq_step_size
    
    return resonant_angular_freq, uncertainty_resonant_freq, fwhh, uncertainty_fwhh


# Component values with tolerance
inductor_value = 150e-3  # 150 mH
capacitor_value = 0.5e-6  # 0.5 μF
tolerance = 0.10  # 10% tolerance

# Calculate theoretical angular frequency and uncertainty
expected_angular_frequency = 1 / np.sqrt(inductor_value * capacitor_value)  # This is ω = 1/√(LC)
uncertainty_expected_frequency = expected_angular_frequency * (tolerance / 2)

# Normalize voltages
one_point_two_k_voltage_normalized = normalize_voltage(one_point_two_k_voltage)
three_point_three_k_voltage_normalized = normalize_voltage(three_point_three_k_voltage)
four_point_five_k_voltage_normalized = normalize_voltage(four_point_five_k_voltage)

# Calculate resonance for each dataset
one_point_two_k_resonance = find_resonance_and_fwhh(one_point_two_k_frequency, one_point_two_k_voltage_normalized)
three_point_three_k_resonance = find_resonance_and_fwhh(three_point_three_k_frequency, three_point_three_k_voltage_normalized)
four_point_five_k_resonance = find_resonance_and_fwhh(four_point_five_k_frequency, four_point_five_k_voltage_normalized)

# Generate LaTeX table with angular frequencies in kHz
def generate_latex_table(resonance_results, expected_freq, expected_freq_uncertainty):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Angular Frequencies and FWHH with Uncertainties}\n"
    latex_table += "\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
    latex_table += "Dataset & Angular Frequency ω (kHz) & FWHH (kHz) & Expected ω (kHz) \\\\ \\hline\n"
    
    for i, resonance in enumerate(resonance_results):
        resonant_freq, uncertainty_resonant_freq, fwhh, uncertainty_fwhh = resonance
        # Convert to angular kHz for display
        resonant_freq_khz = to_angular_khz(resonant_freq)
        uncertainty_khz = to_angular_khz(uncertainty_resonant_freq)
        fwhh_khz = to_angular_khz(fwhh)
        uncertainty_fwhh_khz = to_angular_khz(uncertainty_fwhh)
        expected_freq_khz = to_angular_khz(expected_freq)
        expected_freq_uncertainty_khz = to_angular_khz(expected_freq_uncertainty)
        
        latex_table += f"{['1.2 kΩ', '3.3 kΩ', '4.5 kΩ'][i]} & {resonant_freq_khz:.2f} ± {uncertainty_khz:.2f} & {fwhh_khz:.2f} ± {uncertainty_fwhh_khz:.2f} & {expected_freq_khz:.2f} ± {expected_freq_uncertainty_khz:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Generate table
resonance_results = [one_point_two_k_resonance, three_point_three_k_resonance, four_point_five_k_resonance]
latex_table_output = generate_latex_table(resonance_results, expected_angular_frequency, uncertainty_expected_frequency)

# Print LaTeX table
print(latex_table_output)

# Plotting with angular frequencies in kHz
plt.figure(figsize=(10, 6))
datasets = [
    (one_point_two_k_frequency, one_point_two_k_voltage_normalized, "1.2 kΩ"),
    (three_point_three_k_frequency, three_point_three_k_voltage_normalized, "3.3 kΩ"),
    (four_point_five_k_frequency, four_point_five_k_voltage_normalized, "4.5 kΩ")
]

for freq, volt, label in datasets:
    angular_freq_interp, volt_interp = interpolate_data(freq, volt)
    plt.plot(to_angular_khz(angular_freq_interp), volt_interp, label=label, marker='o')

plt.title('Voltage vs. Angular Frequency for Different Resistances')
plt.xlabel('Angular Frequency ω (kHz)')
plt.ylabel('Normalized Voltage')
plt.legend()
plt.grid()
plt.tight_layout()

# Save the plot
plt.savefig('voltage_vs_angular_frequency_khz.png')
plt.show()


# Function to calculate relative accuracy
def calculate_relative_accuracy(observed_freq, expected_freq):
    return (1 - abs(observed_freq - expected_freq) / expected_freq) * 100

# Calculate relative accuracy for each dataset
one_point_two_k_accuracy = calculate_relative_accuracy(one_point_two_k_resonance[0], expected_angular_frequency)
three_point_three_k_accuracy = calculate_relative_accuracy(three_point_three_k_resonance[0], expected_angular_frequency)
four_point_five_k_accuracy = calculate_relative_accuracy(four_point_five_k_resonance[0], expected_angular_frequency)

# Display results
print("Relative accuracy for each dataset:")
print(f"1.2 kΩ: {one_point_two_k_accuracy:.2f}%")
print(f"3.3 kΩ: {three_point_three_k_accuracy:.2f}%")
print(f"4.5 kΩ: {four_point_five_k_accuracy:.2f}%")
