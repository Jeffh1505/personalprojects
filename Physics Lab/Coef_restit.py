#This code was developed for the first part of lab 1 for PHYS 1494.
#It calculates the coefficient of restitution and error for the coefficient of each trial, the unweighted average and the weighted average.
#Author: Jeffrey Hernandez

import math

#V_i values
v_i_raw = [0.499, 0.711, 0.74, 0.608, 0.833, 0.713, 0.563, 0.731, 0.6, 0.612]
v_i_error = [5.7, 9.3, 4.8, 5.6, 8.1, 5.8, 6.1, 7.7, 5.1, 3.3]

#V_f values
v_f_raw = [-0.434, -0.564, -0.574, -0.508, -0.602, -0.530, -0.48, -0.56, -0.499, -0.508]
v_f_error = [6.2, 3.9, 6.1, 3.9, 6.1, 14, 4, 6, 4.1, 4.2]

coeff_restitution_raw = []
coeff_restitution_error = []

for i in range(len(v_f_raw)):
    if v_i_raw[i] != 0 and v_i_error!= 0:
        coeff_restitution = abs(v_f_raw[i]/v_i_raw[i])
        coeff_restitution_raw.append(float(f"{coeff_restitution:.2g}"))
        coeff_restitution_uncertainty = math.sqrt((v_f_error[i] / v_i_raw[i])**2 + ((v_f_raw[i] * v_i_error[i]) / v_i_raw[i]**2)**2)
        coeff_restitution_error. append(float(f"{coeff_restitution_uncertainty:.2g}"))
    else:
        coeff_restitution_raw.append(float('inf'))
        coeff_restitution_error.append(float("inf"))


print(f"Coefficient of restitutions: {coeff_restitution_raw}")
print(f"Coefficient of restitutions errors: {coeff_restitution_error}")

unweighted_average = sum(coeff_restitution_raw) / len(coeff_restitution_raw)
print(f"Unweighted Average = {unweighted_average}")


sum_for_sigma = 0

for i in range(len(coeff_restitution_raw)):
    sum_for_sigma += (coeff_restitution_raw[i] - unweighted_average)**2

sigma = math.sqrt(sum_for_sigma / (len(coeff_restitution_raw)-1))
print(sigma)

sigma_average = sigma / math.sqrt(len(coeff_restitution_raw))
print(sigma_average)

coeff_sum_for_weighted_average = 0
error_sum_for_weighted_average = 0

for i in range(len(coeff_restitution_raw)):
    coeff_sum_for_weighted_average += coeff_restitution_raw[i] / (coeff_restitution_error[i]**2)
    error_sum_for_weighted_average += 1 / (coeff_restitution_error[i]**2)

weighted_average = coeff_sum_for_weighted_average / error_sum_for_weighted_average

print(weighted_average)

weighted_average_error = 1 / math.sqrt(error_sum_for_weighted_average)

print(weighted_average_error)