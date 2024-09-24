v_i_raw = [0.499, 0.711, 0.74, 0.608, 0.833, 0.713, 0.563, 0.731, 0.6, 0.612]
v_f_raw = [-0.434, -0.564, -0.574, -0.508, -0.602, -0.530, -0.48, -0.56, -0.499, -0.508]

coeff_restitution_raw = []

for i in range(len(v_f_raw)):
    if v_i_raw[i] != 0:
        division = abs(v_f_raw[i]/v_i_raw[i])
        coeff_restitution_raw.append(float(f"{division:.2g}"))
    else:
        coeff_restitution_raw.append(float('inf'))

print(coeff_restitution_raw)