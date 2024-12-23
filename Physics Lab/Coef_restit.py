#This code was developed for the first part of lab 1 for PHYS 1494.
#It calculates the coefficient of restitution and error for the coefficient of each trial, the unweighted average and the weighted average.
#Author: Jeffrey Hernandez

import math
import matplotlib.pyplot as plt

# V_i values (initial velocities)
v_i_raw = [0.499, 0.711, 0.74, 0.608, 0.833, 0.713, 0.563, 0.731, 0.6, 0.612]
v_i_error = [5.7e-4, 9.3e-4, 4.8e-4, 5.6e-4, 8.1e-4, 5.8e-4, 6.1e-4, 7.7e-4, 5.1e-4, 3.3e-4]

# V_f values (final velocities)
v_f_raw = [-0.434, -0.564, -0.574, -0.508, -0.602, -0.530, -0.48, -0.56, -0.499, -0.508]
v_f_error = [6.2e-4, 3.9e-4, 6.1e-4, 3.9e-4, 6.1e-4, 14e-4, 4e-4, 6e-4, 4.1e-4, 4.2e-4]

coeff_restitution_raw = []
coeff_restitution_error = []

for i in range(len(v_f_raw)):
    if v_i_raw[i] != 0 and v_i_error != 0:
        # Calculate coefficient of restitution
        coeff_restitution = abs(v_f_raw[i] / v_i_raw[i])
        coeff_restitution_raw.append(float(f"{coeff_restitution:.3g}"))

        # Calculate uncertainty for the coefficient of restitution
        coeff_restitution_uncertainty = math.sqrt(
            (v_f_error[i] / v_i_raw[i])**2 + ((v_f_raw[i] * v_i_error[i]) / v_i_raw[i]**2)**2
        )
        coeff_restitution_error.append(float(f"{coeff_restitution_uncertainty:.3g}"))
    else:
        coeff_restitution_raw.append(float('inf'))
        coeff_restitution_error.append(float('inf'))

# Print results
print(f"Coefficient of restitutions: {coeff_restitution_raw}")
print(f"Coefficient of restitution errors: {coeff_restitution_error}")

# Unweighted average calculation
unweighted_average = sum(coeff_restitution_raw) / len(coeff_restitution_raw)
print(f"Unweighted Average = {unweighted_average}")

# Calculate sigma (standard deviation)
sum_for_sigma = 0
for i in range(len(coeff_restitution_raw)):
    sum_for_sigma += (coeff_restitution_raw[i] - unweighted_average) ** 2
sigma = math.sqrt(sum_for_sigma / (len(coeff_restitution_raw) - 1))
print(f"Sigma (Standard Deviation) = {sigma}")

# Sigma average
sigma_average = sigma / math.sqrt(len(coeff_restitution_raw))
print(f"Sigma of the average = {sigma_average}")

# Weighted average calculation
coeff_sum_for_weighted_average = 0
error_sum_for_weighted_average = 0

for i in range(len(coeff_restitution_raw)):
    coeff_sum_for_weighted_average += coeff_restitution_raw[i] / (coeff_restitution_error[i] ** 2)
    error_sum_for_weighted_average += 1 / (coeff_restitution_error[i] ** 2)

weighted_average = coeff_sum_for_weighted_average / error_sum_for_weighted_average
print(f"Weighted Average = {weighted_average}")

# Weighted average error
weighted_average_error = 1 / math.sqrt(error_sum_for_weighted_average)
print(f"Weighted Average Error = {weighted_average_error}")

# Visualization
trial_numbers = list(range(1, len(coeff_restitution_raw) + 1))

plt.errorbar(trial_numbers, coeff_restitution_raw, yerr=coeff_restitution_error, fmt='o', ecolor='r', capsize=5, label='Coefficient of Restitution')
plt.axhline(y=unweighted_average, color='g', linestyle='--', label=f'Unweighted Avg = {unweighted_average:.2f}')
plt.axhline(y=weighted_average, color='b', linestyle='-', label=f'Weighted Avg = {weighted_average:.2f}')
plt.xlabel('Trial Number')
plt.ylabel('Coefficient of Restitution')
plt.title('Coefficient of Restitution per Trial with Error Bars')
plt.legend()
plt.grid(True)
plt.show()
