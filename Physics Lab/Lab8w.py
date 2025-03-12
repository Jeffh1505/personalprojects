import numpy as np

# Input data
data = [
    {"color": "Red", "order": 1, "theta_avg_deg": 23.400},
    {"color": "Red", "order": 2, "theta_avg_deg": 52.683},
    {"color": "Cyan", "order": 1, "theta_avg_deg": 17.108},
    {"color": "Cyan", "order": 2, "theta_avg_deg": 36.092},
    {"color": "Blue", "order": 1, "theta_avg_deg": 15.242},
    {"color": "Blue", "order": 2, "theta_avg_deg": 31.725},
    {"color": "Purple", "order": 1, "theta_avg_deg": 29.792},
    {"color": "Purple", "order": 2, "theta_avg_deg": 48.200},
]

d = 1.6058e-6  # Lattice constant (m)
d_uncertainty = 8.2e-9  # Uncertainty in lattice constant (m)
theta_uncertainty_deg = 0.2166666667  # Uncertainty in angle (degrees)

# Helper function to format scientific notation with $$ notation
def format_scientific_latex(num, unc):
    base, exponent = f"{num:.6e}".split("e")
    unc_base, unc_exponent = f"{unc:.6e}".split("e")
    if exponent == unc_exponent:
        return f"$$ {base} \\pm {unc_base} \\times 10^{{{int(exponent)}}} $$"
    return f"$$ {base} \\times 10^{{{int(exponent)}}} \\pm {unc_base} \\times 10^{{{int(unc_exponent)}}} $$"

# Calculate wavelengths and uncertainties
wavelengths_deg = []
wavelength_uncertainties_deg = []

for entry in data:
    theta_avg_deg = entry["theta_avg_deg"]
    m = entry["order"]
    
    # Calculate wavelength using degrees directly
    wavelength = (d * np.sin(theta_avg_deg * (np.pi / 180))) / m
    
    # Uncertainty calculation
    partial_d = np.sin(theta_avg_deg * (np.pi / 180)) / m
    partial_theta = (d * np.cos(theta_avg_deg * (np.pi / 180)) * (np.pi / 180)) / m
    wavelength_uncertainty = np.sqrt((partial_d * d_uncertainty) ** 2 +
                                     (partial_theta * theta_uncertainty_deg) ** 2)
    
    # Append results
    wavelengths_deg.append(wavelength)
    wavelength_uncertainties_deg.append(wavelength_uncertainty)

# Calculate weighted averages for each color
color_groups = {}
for entry in data:
    color = entry["color"]
    if color not in color_groups:
        color_groups[color] = []
    color_groups[color].append(entry)

weighted_avg_wavelengths_deg = {}
for color, values in color_groups.items():
    wls = [wavelengths_deg[data.index(entry)] for entry in data if entry["color"] == color]
    unc = [wavelength_uncertainties_deg[data.index(entry)] for entry in data if entry["color"] == color]
    weights = 1 / np.array(unc) ** 2
    weighted_avg = np.sum(weights * np.array(wls)) / np.sum(weights)
    weighted_unc = np.sqrt(1 / np.sum(weights))
    weighted_avg_wavelengths_deg[color] = (weighted_avg, weighted_unc)

# Generate LaTeX tables
latex_table = "\\begin{table}[H]\n\\centering\n\\caption{Calculated Wavelengths (Using Degrees)}\n"
latex_table += "\\label{table:calculated-wavelengths-degrees}\n\\begin{tabular}{|c|c|c|}\n"
latex_table += "\\hline\nColor & Order & Wavelength (m) \\\\\n\\hline\n"

for entry, wl, wl_unc in zip(data, wavelengths_deg, wavelength_uncertainties_deg):
    latex_table += f"{entry['color']} & {entry['order']} & {format_scientific_latex(wl, wl_unc)} \\\\\n"

latex_table += "\\hline\n\\end{tabular}\n\\end{table}\n\n"

latex_table += "\\begin{table}[H]\n\\centering\n\\caption{Weighted Average Wavelengths (Using Degrees)}\n"
latex_table += "\\label{table:weighted-average-wavelengths-degrees}\n\\begin{tabular}{|c|c|}\n"
latex_table += "\\hline\nColor & Weighted Average Wavelength (m) \\\\\n\\hline\n"

for color, (avg, unc) in weighted_avg_wavelengths_deg.items():
    latex_table += f"{color} & {format_scientific_latex(avg, unc)} \\\\\n"

latex_table += "\\hline\n\\end{tabular}\n\\end{table}"

# Print LaTeX tables
print(latex_table)
