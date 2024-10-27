import numpy as np

# Circuit parameters with 10% tolerances
L = 150e-3            # Inductance (150 mH)
L_uncertainty = L * 0.10
C = 0.5e-6            # Capacitance (0.5 μF)
C_uncertainty = C * 0.10
R = 3.3e3             # Resistance (3.3 kΩ)
R_uncertainty = R * 0.10

# Data for inductor and capacitor
inductor_data = {
    "frequency_kHz": 10.27,
    "time_difference_microsec": 18,
    "total_time_difference_microsec": 98
}

capacitor_data = {
    "frequency_Hz": 20.6,
    "time_difference_millisec": 9.6,
    "total_time_difference_microsec": 48.4
}

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

# Calculate phase difference for inductor data
frequency_inductor = inductor_data["frequency_kHz"] * 1e3  # Convert kHz to Hz
phase_diff_inductor_pi, phase_diff_inductor_uncertainty_pi = calculate_phase_difference_pi(
    frequency_inductor, inductor_data["time_difference_microsec"]
)

# Calculate phase difference for capacitor data
frequency_capacitor = capacitor_data["frequency_Hz"]
phase_diff_capacitor_pi, phase_diff_capacitor_uncertainty_pi = calculate_phase_difference_pi(
    frequency_capacitor, capacitor_data["time_difference_millisec"] * 1e3  # Convert ms to µs
)

# Generate LaTeX table with ± for uncertainties
def generate_latex_table_inductor_capacitor(phase_inductor, uncertainty_inductor, phase_capacitor, uncertainty_capacitor):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Phase Difference with Uncertainties for Inductor and Capacitor}\n"
    latex_table += "\\begin{tabular}{|c|c|c|}\n\\hline\n"
    latex_table += "Component & Calculated Phase ($\\pi$) & Uncertainty ($\\pm$ $\\pi$) \\\\ \\hline\n"
    
    # Add inductor data
    latex_table += f"Inductor & {phase_inductor:.2f} & {uncertainty_inductor:.2f} \\\\ \\hline\n"
    
    # Add capacitor data
    latex_table += f"Capacitor & {phase_capacitor:.2f} & {uncertainty_capacitor:.2f} \\\\ \\hline\n"
    
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Print LaTeX table for phase differences
latex_table_output = generate_latex_table_inductor_capacitor(
    phase_diff_inductor_pi, phase_diff_inductor_uncertainty_pi,
    phase_diff_capacitor_pi, phase_diff_capacitor_uncertainty_pi
)
print(latex_table_output)
