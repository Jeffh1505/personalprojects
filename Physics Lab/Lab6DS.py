import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def analyze_diffraction_pattern(maxima_positions, minima_positions, d, L, d_uncertainty, L_uncertainty, position_uncertainty=0.001):
    """
    Analyze both maxima and minima from diffraction pattern to find wavelength and slit width.
    
    Parameters:
    maxima_positions (array): Positions of maxima in meters
    minima_positions (list): List of minima positions (without the -4 minima)
    d (float): Slit separation in meters
    L (float): Screen distance in meters
    d_uncertainty (float): Uncertainty in slit separation (meters)
    L_uncertainty (float): Uncertainty in screen distance (meters)
    position_uncertainty (float): Uncertainty in position measurements (meters)
    """
    # Ensure minima_positions is a numpy array and remove the -4 minima
    minima_positions = np.array(minima_positions)
    
    # Remove the "bad" minima at index 3 (which corresponds to -4 order)
    minima_positions = np.delete(minima_positions, 3)
    
    # Analyze maxima
    order_numbers_max = np.arange(-(len(maxima_positions) - 1) // 2, (len(maxima_positions)) // 2 + 1)
    position_uncertainties_max = np.full_like(maxima_positions, position_uncertainty)
    
    # Perform linear regression for maxima
    slope_max, intercept_max, r_value_max, p_value_max, std_err_max = linregress(order_numbers_max, maxima_positions)
    
    # Calculate wavelength
    wavelength = slope_max * d / L * 1e9  # Convert to nanometers
    
    # Error propagation for wavelength
    uncertainty_from_slope = (std_err_max * d / L) * 1e9
    uncertainty_from_d = (slope_max * d_uncertainty / L) * 1e9
    uncertainty_from_L = (slope_max * d * L_uncertainty / (L * L)) * 1e9
    wavelength_uncertainty = np.sqrt(uncertainty_from_slope**2 + uncertainty_from_d**2 + uncertainty_from_L**2)
    
    # Plot maxima
    fig_max = plt.figure(figsize=(8, 6))
    ax1 = fig_max.add_subplot(111)
    x_fit_max = np.linspace(order_numbers_max.min(), order_numbers_max.max(), 100)
    y_fit_max = slope_max * x_fit_max + intercept_max
    
    ax1.errorbar(order_numbers_max, maxima_positions, 
                yerr=position_uncertainties_max,
                fmt='o', color='blue', 
                capsize=5,
                label='Measured Maxima')
    ax1.plot(x_fit_max, y_fit_max, color='red', linestyle='-', 
            label=f'Best Fit Line\nslope = {slope_max:.3e} m/order')
    ax1.axhline(0, color='black', linewidth=0.8, linestyle='-')
    ax1.axvline(0, color='black', linewidth=0.8, linestyle='-')
    ax1.set_xlabel('Order of Maxima')
    ax1.set_ylabel('Position (m)')
    ax1.set_title('Maxima Analysis')
    ax1.legend()
    ax1.grid(True)
    plt.tight_layout()
    plt.show()  # Explicit call to display maxima plot
    
    # Analyze minima (remove the "-4" minima point)
    order_numbers_min = np.arange(-(len(minima_positions) - 1) // 2, (len(minima_positions) + 1) // 2)  # Match length of minima_positions
    position_uncertainties_min = np.full_like(minima_positions, position_uncertainty)
    
    # Perform linear regression for minima
    slope_min, intercept_min, r_value_min, p_value_min, std_err_min = linregress(order_numbers_min, minima_positions)
    
    # Calculate slit width (a = mλ/sin(θ) ≈ mλL/y)
    wavelength_m = wavelength * 1e-9  # Convert wavelength to meters
    slit_width = wavelength_m / (slope_min / L)
    
    # Error propagation for slit width
    relative_wavelength_uncertainty = wavelength_uncertainty / wavelength
    relative_slope_uncertainty = std_err_min / slope_min
    relative_uncertainty = np.sqrt(relative_wavelength_uncertainty**2 + relative_slope_uncertainty**2)
    slit_width_uncertainty = slit_width * relative_uncertainty
    
    # Plot minima
    fig_min = plt.figure(figsize=(8, 6))
    ax2 = fig_min.add_subplot(111)
    x_fit_min = np.linspace(order_numbers_min.min(), order_numbers_min.max(), 100)
    y_fit_min = slope_min * x_fit_min + intercept_min
    
    ax2.errorbar(order_numbers_min, minima_positions, 
                yerr=position_uncertainties_min,
                fmt='o', color='blue', 
                capsize=5,
                label='Measured Minima')
    ax2.plot(x_fit_min, y_fit_min, color='red', linestyle='-', 
            label=f'Best Fit Line\nslope = {slope_min:.3e} m/order')
    ax2.axhline(0, color='black', linewidth=0.8, linestyle='-')
    ax2.axvline(0, color='black', linewidth=0.8, linestyle='-')
    ax2.set_xlabel('Order of Minima')
    ax2.set_ylabel('Position (m)')
    ax2.set_title('Minima Analysis (Without -4)')
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.show()  # Explicit call to display minima plot
    
    # Generate LaTeX tables for maxima and minima positions
    def generate_latex_table(order_numbers, positions, label):
        latex_str = f"\\begin{{table}}[h!]\n\\centering\n\\begin{{tabular}}{{|c|c|}}\n\\hline\n"
        latex_str += f"Order of {label} & Position (m) \\\\ \\hline\n"
        for order, position in zip(order_numbers, positions):
            latex_str += f"{order} & {position:.6f} \\\\ \\hline\n"
        latex_str += "\\end{tabular}\n\\caption{Position data for " + label + "}\n\\end{table}\n"
        return latex_str
    
    # Print LaTeX tables for maxima and minima
    latex_maxima = generate_latex_table(order_numbers_max, maxima_positions, "Maxima")
    latex_minima = generate_latex_table(order_numbers_min, minima_positions, "Minima")
    
    print("\nLaTeX Table for Maxima:")
    print(latex_maxima)
    
    print("\nLaTeX Table for Minima:")
    print(latex_minima)
    
    # Print results
    print("\nMaxima Analysis Results:")
    print(f"Wavelength: {wavelength:.2f} ± {wavelength_uncertainty:.2f} nm")
    print(f"R-squared: {r_value_max**2:.4f}")
    
    print("\nMinima Analysis Results:")
    print(f"Slit Width: {slit_width*1e6:.2f} ± {slit_width_uncertainty*1e6:.2f} μm")
    print(f"R-squared: {r_value_min**2:.4f}")
    
    return wavelength, wavelength_uncertainty, slit_width, slit_width_uncertainty

# Example usage with your data (excluding the -4 minima point)
maxima_positions = np.array([0.017, 0.036, 0.052, 0.078, 0.104, 0.119, 0.138]) * 0.1
minima_positions = [0.015, 0.031, 0.046, 0.062, 0.093, 0.109, 0.124, 0.138]  # Provided data, without -4 minima
d = 0.00025
L = 0.98
d_uncertainty = 0.00001
L_uncertainty = 0.02

wavelength, wavelength_unc, slit_width, slit_width_unc = analyze_diffraction_pattern(
    maxima_positions, minima_positions, d, L, d_uncertainty, L_uncertainty)
