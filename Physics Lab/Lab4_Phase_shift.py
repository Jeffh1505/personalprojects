import numpy as np

# Data: Frequency in Hz and Time Difference in microseconds
data = [
    (184.2, 320),
    (381, 80),
    (581.3, 40),
    (776.3, 40),
    (981, -40)
]

# Circuit parameters with uncertainties (10% tolerance)
L = 150e-3            # Inductance (150 mH)
L_uncertainty = L * 0.10
C = 0.5e-6            # Capacitance (0.5 μF)
C_uncertainty = C * 0.10
R = 3.3e3             # Resistance (3.3 kΩ)
R_uncertainty = R * 0.10

# Function to calculate phase difference in terms of pi and its uncertainty
def calculate_phase_difference_pi(frequency, time_difference_micro):
    # Convert time difference from microseconds to seconds
    time_difference = time_difference_micro * 1e-6
    # Calculate the period of the signal
    period = 1 / frequency
    # Calculate phase difference in radians and in terms of pi
    phase_difference_radians = (time_difference / period) * 2 * np.pi
    phase_difference_pi = phase_difference_radians / np.pi

    # Calculate uncertainty in phase difference (propagation of frequency uncertainty)
    frequency_uncertainty = frequency * 0.10  # Assuming 10% frequency tolerance
    period_uncertainty = frequency_uncertainty / (frequency**2)  # dT/dF = -1/f^2
    phase_difference_uncertainty_radians = (time_difference / (period**2)) * 2 * np.pi * period_uncertainty
    phase_difference_uncertainty_pi = phase_difference_uncertainty_radians / np.pi

    return phase_difference_pi, phase_difference_uncertainty_pi

# Function to calculate expected phase difference and its uncertainty
def expected_phase_difference_pi(frequency):
    omega = 2 * np.pi * frequency
    term1 = omega * L
    term2 = 1 / (omega * C)
    phase_difference_radians = np.arctan((term1 - term2) / R)
    phase_difference_pi = phase_difference_radians / np.pi

    # Uncertainty propagation
    d_phi_dL = (omega / R) / (1 + ((term1 - term2) / R)**2)
    d_phi_dC = (1 / (omega**2 * C**2 * R)) / (1 + ((term1 - term2) / R)**2)
    d_phi_dR = -((term1 - term2) / (R**2)) / (1 + ((term1 - term2) / R)**2)
    
    phase_difference_uncertainty_radians = np.sqrt(
        (d_phi_dL * L_uncertainty)**2 +
        (d_phi_dC * C_uncertainty)**2 +
        (d_phi_dR * R_uncertainty)**2
    )
    phase_difference_uncertainty_pi = phase_difference_uncertainty_radians / np.pi

    return phase_difference_pi, phase_difference_uncertainty_pi

# Calculate phase differences and store results
results = []
for freq, time_diff in data:
    calculated_phase_diff_pi, calculated_phase_uncertainty_pi = calculate_phase_difference_pi(freq, time_diff)
    expected_phase_diff_pi, expected_phase_uncertainty_pi = expected_phase_difference_pi(freq)
    results.append((freq, time_diff, calculated_phase_diff_pi, calculated_phase_uncertainty_pi, expected_phase_diff_pi, expected_phase_uncertainty_pi))

# Generate LaTeX table with ± for uncertainties
def generate_latex_table(results):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Phase Difference with Uncertainties Compared to Expected Values}\n"
    latex_table += "\\begin{tabular}{|c|c|c|c|c|c|}\n\\hline\n"
    latex_table += "Frequency (Hz) & Time Diff (µs) & Calculated Phase ($\\pi$) & Expected Phase ($\\pi$) \\\\ \\hline\n"
    
    for freq, time_diff, calc_phase_pi, calc_uncertainty_pi, exp_phase_pi, exp_uncertainty_pi in results:
        latex_table += f"{freq:.1f} & {time_diff} & {calc_phase_pi:.2f} ± {calc_uncertainty_pi:.2f} $\\pi$ & {exp_phase_pi:.2f} ± {exp_uncertainty_pi:.2f} $\\pi$ \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Print LaTeX table
latex_table_output = generate_latex_table(results)
print(latex_table_output)
