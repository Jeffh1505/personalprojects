import numpy as np

# Experimentally found resonant frequency (in Hz) and its uncertainty
resonant_frequency_exp = 1179.6  # Example value in Hz
resonant_frequency_uncertainty = 5  # Example uncertainty in Hz

# Known component for the calculation (Capacitance in Farads)
capacitance = 0.5e-6  # 0.5 μF

# Expected inductance value and 10% tolerance
expected_inductance = 35.9e-3  # 150 mH
inductance_tolerance = 0.10 * expected_inductance  # 10% tolerance

# Calculated inductance based on experimentally found resonant frequency
# Formula: L = 1 / (C * (2πf)^2)
resonant_angular_freq = 2 * np.pi * resonant_frequency_exp
calculated_inductance = 1 / (capacitance * resonant_angular_freq ** 2)

# Uncertainty in calculated inductance
# Derived by propagating uncertainty in frequency: ΔL/L = 2 * Δf/f
calculated_inductance_uncertainty = calculated_inductance * 2 * (resonant_frequency_uncertainty / resonant_frequency_exp)

# Convert inductances to mH for reporting
expected_inductance_mH = expected_inductance * 1e3
inductance_tolerance_mH = inductance_tolerance * 1e3
calculated_inductance_mH = calculated_inductance * 1e3
calculated_inductance_uncertainty_mH = calculated_inductance_uncertainty * 1e3

# Generate LaTeX table
def generate_latex_table(resonant_freq, res_freq_unc, calc_ind, calc_ind_unc, exp_ind, exp_ind_tol):
    latex_table = "\\begin{table}[h!]\n\\centering\n\\caption{Resonant Frequency and Inductance Measurements with Uncertainties}\n"
    latex_table += "\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
    latex_table += "Resonant Frequency (Hz) & Calculated Inductance (mH) & Expected Inductance (mH) \\\\ \\hline\n"
    latex_table += f"{resonant_freq:.0f} ± {res_freq_unc:.0f} & {calc_ind:.2f} ± {calc_ind_unc:.2f} & {exp_ind:.2f} ± {exp_ind_tol:.2f} \\\\ \\hline\n"
    latex_table += "\\end{tabular}\n\\end{table}"
    return latex_table

# Print LaTeX table
latex_table_output = generate_latex_table(
    resonant_frequency_exp,
    resonant_frequency_uncertainty,
    calculated_inductance_mH,
    calculated_inductance_uncertainty_mH,
    expected_inductance_mH,
    inductance_tolerance_mH
)

print(latex_table_output)
