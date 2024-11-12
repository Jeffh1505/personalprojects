import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate, optimize

# Physical constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T·m/A)
N = 132     # Number of turns in the coil
R = 0.1475  # Radius of coil (m)
C = (mu_0 * N) / (R * (1 + (1/4))**(3/2))  # Geometric constant

def format_scientific(value, uncertainty):
    exponent = int(np.floor(np.log10(abs(value))))
    scaled_value = value / 10**exponent
    scaled_uncertainty = uncertainty / 10**exponent
    return f"{scaled_value:.2f} ± {scaled_uncertainty:.2f} × 10^{exponent}"

def interpolate_data(radius_cm, current_A, target_radius=5.0):
    sort_idx = np.argsort(radius_cm)
    radius_sorted = np.array(radius_cm)[sort_idx]
    current_sorted = np.array(current_A)[sort_idx]

    if min(radius_sorted) > target_radius:
        f = interpolate.interp1d(radius_sorted, current_sorted, fill_value='extrapolate', kind='linear')
        radius_new = np.append([target_radius], radius_sorted)
        current_new = np.append([f(target_radius)], current_sorted)
        return radius_new, current_new
    
    unique_radius, unique_idx = np.unique(radius_sorted, return_index=True)
    unique_current = current_sorted[unique_idx]
    duplicate_indices = np.where(np.diff(radius_sorted) == 0)[0]
    
    for idx in duplicate_indices:
        start = idx
        end = next((i for i, x in enumerate(radius_sorted[idx+1:], idx+1) if x != radius_sorted[idx]), len(radius_sorted))
        avg_current = np.mean(current_sorted[start:end])
        current_sorted[idx] = avg_current
    
    f = interpolate.interp1d(unique_radius, unique_current, fill_value='extrapolate', kind='linear')
    return np.append([target_radius], unique_radius), np.append([f(target_radius)], unique_current)

def load_voltage_data(radius_cm, current_A):
    radius_m = np.array(radius_cm) / 100
    current = np.array(current_A)
    current_error = 0.05 * current
    radius_error = 0.005
    inverse_radius = 1 / radius_m
    inverse_radius_error = (inverse_radius**2) * radius_error
    return inverse_radius, current, current_error, inverse_radius_error

def linear_model(x, slope, intercept):
    return slope * x + intercept

def weighted_linear_regression(x, y, yerr):
    valid_indices = np.isfinite(x) & np.isfinite(y) & np.isfinite(yerr)
    x_valid = x[valid_indices]
    y_valid = y[valid_indices]
    yerr_valid = yerr[valid_indices]
    
    popt, pcov = optimize.curve_fit(linear_model, x_valid, y_valid, sigma=yerr_valid, absolute_sigma=True)
    slope, intercept = popt
    slope_err, intercept_err = np.sqrt(np.diag(pcov))
    return slope, intercept, slope_err, intercept_err

def charge_to_mass_from_slope(slope, V):
    return (2 * V) / (C * slope)**2

def plot_data_and_fits(data_sets, fits):
    plt.figure(figsize=(10, 6))
    colors = ['r', 'g', 'b', 'y']
    
    for (voltage, inv_radius, current, current_error, inv_radius_error), fit, color in zip(data_sets, fits, colors):
        plt.errorbar(inv_radius, current, 
                     xerr=inv_radius_error,
                     yerr=current_error, 
                     fmt='o', label=f'{voltage}V - Experimental', 
                     capsize=5, color=color)
        x_fit = np.linspace(min(inv_radius), max(inv_radius), 100)
        plt.plot(x_fit, linear_model(x_fit, *fit[:2]), 
                 '--', label=f'{voltage}V - Fit', 
                 color=color)
    
    plt.xlabel('1/r (m⁻¹)')
    plt.ylabel('Current (A)')
    plt.title('Current vs 1/r for Different Voltages with Best-Fit Lines')
    plt.legend()
    plt.grid(True)
    plt.show()

def create_latex_table(fits, voltages, em_ratios):
    latex_table = r"""
    \begin{table}[ht]
    \centering
    \resizebox{\columnwidth}{!}{%
    \begin{tabular}{|c|c|c|c|} 
    \hline
    Voltage (V) & Slope (A·m) & Intercept (A) & Charge-to-Mass Ratio (C/kg) \\ \hline
    """
    
    for voltage, fit, em_ratio in zip(voltages, fits, em_ratios):
        slope, intercept, slope_err, intercept_err = fit
        em_uncertainty = np.abs(em_ratio) * 2 * (slope_err / slope)
        
        em_formatted = format_scientific(em_ratio, em_uncertainty).replace('×', r'\times')
        slope_formatted = format_scientific(slope, slope_err).replace('×', r'\times')
        intercept_formatted = format_scientific(intercept, intercept_err).replace('×', r'\times')
        
        latex_table += f"{voltage} & {slope_formatted} & {intercept_formatted} & {em_formatted} \\\\ \\hline\n"
    
    latex_table += r"""
    \end{tabular}%
    }
    \caption{Linear Fit Results for Current vs 1/r and Charge-to-Mass Ratio for Different Voltages.}
    \label{tab:results}
    \end{table}
    """
    return latex_table

def calculate_weighted_average(values, uncertainties):
    weights = 1.0 / (uncertainties ** 2)
    weighted_avg = np.sum(values * weights) / np.sum(weights)
    weighted_uncertainty = np.sqrt(1.0 / np.sum(weights))
    
    exponent = int(np.floor(np.log10(abs(weighted_avg))))
    scaled_avg = weighted_avg / 10**exponent
    scaled_uncertainty = weighted_uncertainty / 10**exponent
    return weighted_avg, weighted_uncertainty, scaled_avg, scaled_uncertainty, exponent

if __name__ == "__main__":
    raw_data_sets = [
        (200, [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11], [2.05, 1.83, 1.65, 1.54, 1.42, 1.34, 1.29, 1.21, 1.16, 1.12, 1.07, 1.02, 0.97]),
        (300, [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11], [2.5, 2.25, 2.03, 1.87, 1.78, 1.64, 1.56, 1.44, 1.36, 1.28, 1.2, 1.12, 1.05]),
        (400, [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11], [3.05, 2.75, 2.43, 2.27, 2.08, 1.94, 1.86, 1.74, 1.66, 1.58, 1.5, 1.42, 1.35]),
        (500, [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11], [3.6, 3.29, 2.96, 2.71, 2.54, 2.36, 2.28, 2.06, 1.94, 1.82, 1.71, 1.64, 1.56])
    ]

    processed_data_sets = []
    fits = []
    voltages = [200, 300, 400, 500]

    for voltage, radius, current in raw_data_sets:
        inv_radius, current_array, current_error, inv_radius_error = load_voltage_data(radius, current)
        fit = weighted_linear_regression(inv_radius, current_array, current_error)
        processed_data_sets.append((voltage, inv_radius, current_array, current_error, inv_radius_error))
        fits.append(fit)
    
    em_ratios = []
    em_uncertainties = []

    for (voltage, inv_radius, current_array, current_error, inv_radius_error), (slope, _, slope_err, _) in zip(processed_data_sets, fits):
        em_ratio = charge_to_mass_from_slope(slope, voltage)
        em_uncertainty = np.abs(em_ratio) * 2 * (slope_err / slope)
        em_ratios.append(em_ratio)
        em_uncertainties.append(em_uncertainty)
    
    weighted_avg_em, weighted_uncertainty_em, scaled_avg, scaled_uncertainty, exponent = calculate_weighted_average(np.array(em_ratios), np.array(em_uncertainties))
    latex_table = create_latex_table(fits, voltages, em_ratios)

    plot_data_and_fits(processed_data_sets, fits)
    print("LaTeX Table:")
    print(latex_table)
    print(f"\nWeighted Average e/m: ({scaled_avg:.2f} ± {scaled_uncertainty:.2f}) × 10^{exponent} C/kg")
