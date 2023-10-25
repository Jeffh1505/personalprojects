import numpy as np
from matplotlib import pyplot as plt

# Initialization
Wpl_max = 1.0  # Max payload weight for M2
M2_min = 1.0 # Minimum time for M2 (ideal to keep completion time as low as possible)
bc_max = 1.0  # Max battery capacity
laps_max = 1.0 # Max number of laps for M3
Pas_max = 1.0  # Max number of passengers for M3

Wpl = 0.5 * Wpl_max  # Payload weight for M2
M2 = 0.5* M2_min # Time for M2
bc = 0.5 * bc_max  # Battery capacity
laps = 0.5 * laps_max # Number of laps for M3
Pas = 0.5 * Pas_max  # Number of passengers for M3
parameters = np.array([Wpl, M2, bc, laps, Pas], dtype='float')
parameters_max = np.array([Wpl_max, M2_min, bc_max, laps_max, Pas_max], dtype='float')
# Arrays created to store values generated during sensitivity analysis

def M2(parameters, parameters_max):
    payload_weight_time = parameters[0] / parameters[1]
    max_payload_weight_time = parameters_max[1] / parameters_max[1]
    if max_payload_weight_time == 0:
        max_payload_weight_time = 1  # Avoid division by zero
    return 1 + (payload_weight_time / max_payload_weight_time)

def M3(parameters, parameters_max):
    laps_passengers_capacity = (parameters[3] * parameters[4]) / parameters[2]
    max_laps_passengers_capacity = (parameters_max[3] * parameters_max[4]) / parameters_max[2]
    if max_laps_passengers_capacity == 0:
        max_laps_passengers_capacity = 1  # Avoid division by zero
    return 2 + (laps_passengers_capacity / max_laps_passengers_capacity)

def total(parameters, parameters_max):
    return M2(parameters, parameters_max) + M3(parameters, parameters_max)
# All definitions from scoring equations given in 2024 rule set
# M1 was excluded since participation in other missions depends on successful M1 completion--taken as given
def vary_param(parameters, parameters_max, param_index, p):
    proportion_change = p
    x = np.linspace(-proportion_change, proportion_change)
    x_param = np.array([parameters[param_index] * (1 + p) for p in x])
    x = x * 100
    y = []

    for param in x_param:
        parameters_new = np.copy(parameters)
        parameters_new[param_index] = param
        y.append((total(parameters_new, parameters_max) - total(parameters, parameters_max)) / total(parameters, parameters_max) * 100)

    return x, y
# vary_param takes a parameter index (param_index) and a proportion change (p) as inputs.
# It varies the specified parameter within a certain range around its initial value 
# and records how it affects the total mission score. 
# It returns two arrays, x and y, which represent the percentage change in the parameter and the percentage change in the total mission score, respectively.
def label(i):
    label = ''
    if (i == 0):
        label = 'Payload weight for M2'
    if (i == 1):
        label = 'M2 Time'
    if (i == 2):
        label = 'Battery capacity'
    if (i == 3):
        label = 'Number of Laps in M3'
    if (i == 4):
        label = 'Number of Passengers in M3'
    return label

fig, plot = plt.subplots(1, 1, figsize=(10, 8))

line_styles = ['-', '--', ':', '-', '-.']
line_colors = ['blue', 'orange', 'green', 'black', 'yellow'] 
# I had to add in specific colors and line styles because the lines for i=3 and i=4 overlapped 
# and I had to make sure they contrasted well enough to tell them apart

for i in [0, 1, 2, 3, 4]:
    x, y = vary_param(parameters, parameters_max, i, 1)
    label_text = label(i)
    plot.plot(x, y, label=label_text, linestyle=line_styles[i], color=line_colors[i])
# Everything above here was used for the plot legend and graphs, it should be pretty self-explanatory
plot.set_xlim(-80, 80)
plot.set_ylim(-10, 15)
plot.set_xlabel('% Change in Parameter', fontsize=16)
plot.set_ylabel('% Change in Total Mission Score', fontsize=16)
plot.set_title('Sensitivity Analysis', fontsize=18)
plot.grid(alpha=0.5)

plt.legend(loc='upper right')
#plt.savefig('sensitivity_final.png')
plt.show()
