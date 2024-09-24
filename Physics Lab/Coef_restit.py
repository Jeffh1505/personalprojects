#V_i values
v_i_raw = [0.499, 0.711, 0.74, 0.608, 0.833, 0.713, 0.563, 0.731, 0.6, 0.612]
v_i_error = [0.00327, 0.00306, 0.0014, 0.0024, 0.00196, 0.00112, 0.00285, 0.00243, 0.00209, 0.00118]

#V_f values
v_f_raw = [-0.434, -0.564, -0.574, -0.508, -0.602, -0.530, -0.48, -0.56, -0.499, -0.508]
v_f_error = [0.00421, 0.00182, 0.00278, 0.00209, 0.0026, 0.00712, 0.00244, 0.00281, 0.00229, 0.00221]

coeff_restitution_raw = []
coeff_restitution_error = []

for i in range(len(v_f_raw)):
    if v_i_raw[i] != 0 and v_i_error!= 0:
        coeff_restitution = abs(v_f_raw[i]/v_i_raw[i])
        coeff_restitution_raw.append(float(f"{coeff_restitution:.2g}"))
        coeff_restitution_uncertantiy = abs(v_f_error[i]/v_i_error[i])
        coeff_restitution_error. append(float(f"{coeff_restitution_uncertantiy:.2g}"))
    else:
        coeff_restitution_raw.append(float('inf'))
        coeff_restitution_error.append(float("inf"))


print(coeff_restitution_raw)
print(coeff_restitution_error)
