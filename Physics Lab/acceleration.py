#This code was developed for the first part of lab 1 for PHYS 1494.
#It calculates the acceleration due to gravity and error for the acceleration due to gravity.
#Author: Jeffrey Hernandez

import math
import matplotlib.pyplot as plt 
import numpy as np
import scipy.optimize as opt

# Data
experiement_1_data = [0.0154, 0.0156, 0.0171, 0.0157, 0.0154, 0.0166, 0.0155, 0.0161, 0.0153, 0.0161]
experiement_1_error = [1.3, 11.0, 1.5, 12.0, 10.0, 13.0, 10.0, 4.4, 12.0, 1.1]
h_1 = 0.001

experiement_2_data = [0.0308, 0.0296, 0.0299, 0.0288, 0.0296, 0.0297, 0.0293, 0.0287, 0.0286, 0.0301]
experiement_2_error = [7.6, 18.0, 6.5, 16.00, 16.0, 7.5, 17.0, 17.0, 15.0, 16.0]
h_2 = 0.0024

experiement_3_data = [0.0410, 0.0414, 0.0427, 0.0433, 0.0432, 0.0424, 0.0422, 0.0427, 0.0434, 0.0396]
experiement_3_error = [18.0, 14.0, 15.0, 13.0, 20.0, 16.0, 12.0, 13.0, 11.0, 18.0]
h_3 = 0.0036

experiement_4_data = [0.0538, 0.0511, 0.0538, 0.0504, 0.0506, 0.0524, 0.0518, 0.0503, 0.0501, 0.0510]
experiement_4_error = [6.1, 16.0, 19.0, 18.0, 19.0, 19.0, 19.0, 19.0, 16.0, 18.0]
h_4 = 0.0049

experiement_5_data = [0.0642, 0.0648, 0.0643, 0.0659, 0.0632, 0.0645, 0.0641, 0.0629, 0.0641, 0.0658]
experiement_5_error = [19.0, 40.0, 19.0, 13.0, 15.0, 10.0, 14.0, 17.0, 10.0,13.0]
h_5 = 0.0063

# Function for unweighted stats
def unweighted_stats(a1:list) -> tuple:
    unweighted_average = sum(a1)/ len(a1)
    sum_for_sigma = sum((x - unweighted_average)**2 for x in a1)
    sigma = math.sqrt(sum_for_sigma / (len(a1) - 1))
    sigma_average = sigma / math.sqrt(len(a1))
    return unweighted_average, sigma_average

# Rounds a number to 2 significant figures
def round_to_sigfigs(x, sigfigs=2):
    if x == 0:
        return 0
    return round(x, sigfigs - int(math.floor(math.log10(abs(x)))) - 1)

# Data list
data_list = [experiement_1_data, experiement_2_data, experiement_3_data, experiement_4_data, experiement_5_data]
h_list = [h_1, h_2, h_3, h_4, h_5]

average_a_list = []
average_error_list = []

# Calculating averages and errors
for i in range(len(data_list)):
    a_avg, sigma_avg = unweighted_stats(data_list[i])
    average_a_list.append(a_avg)
    average_error_list.append(sigma_avg)

# Rounding the average accelerations and errors to 2 significant figures
rounded_avg_a_list = [round_to_sigfigs(a, 3) for a in average_a_list]
rounded_avg_error_list = [round_to_sigfigs(sigma, 3) for sigma in average_error_list]
rounded_avg_error_list_scaled = [round_to_sigfigs(sigma * 1e4, 3) for sigma in average_error_list]  # Scaled errors

print("Average acceleration values (2 significant figures):", rounded_avg_a_list)
print("Average error values (2 significant figures, as multiples of 10⁻⁴):", rounded_avg_error_list_scaled)

# Initial guess for curve fitting
x0 = np.array([0.0, 0.0])

# Define linear function for fitting
def funclin(x, a, b):
    return a + b*x

# Perform curve fitting using the original (non-rounded) data
pars, w = opt.curve_fit(funclin, h_list, average_a_list, x0, average_error_list, absolute_sigma=True)
err = np.sqrt(np.diag(w))

# Calculating g and its error, rounding to 2 significant figures
g = round_to_sigfigs(pars[1], 2)
sigma_g_scaled = round_to_sigfigs(err[1] * 1e4, 2)  # Multiply by 10^4 and round to 2 significant figures

print(f"g = {g} m/s^2")
print(f"Sigma_g = {sigma_g_scaled} × 10⁻⁴ m/s²")



# Plotting the data and fit using the original (unscaled) errors for the plot
fit = funclin(np.array(h_list), *pars)

plt.figure(figsize=(10,6))
plt.errorbar(h_list, average_a_list, average_error_list, 
             marker='o', color='blue', ecolor='black', 
             mec='red', linestyle='None', ms=8, mew=2, label="Data")

plt.plot(h_list, fit, color='green', linestyle='-', linewidth=2, label="Linear fit")

# Adding labels, grid, and title
plt.xlabel('Height (h) in meters', fontsize=14)
plt.ylabel('Acceleration (a) in $m/s^2$', fontsize=14)
plt.title('Relationship between Height and Acceleration', fontsize=16)

# Display slope (g) and intercept on the graph
slope_text = f"Slope (g) = {g} m/s²"
intercept_text = f"Intercept = {round_to_sigfigs(pars[0], 2)} m/s²"
plt.text(0.002, min(average_a_list) + 0.001, slope_text, fontsize=12, color='green')
plt.text(0.002, min(average_a_list) + 0.004, intercept_text, fontsize=12, color='green')

plt.legend(loc='best', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.7)
plt.minorticks_on()

# Enhancing tick size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
