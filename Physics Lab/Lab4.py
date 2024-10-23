import numpy as np
import matplotlib.pyplot as plt

# Data
one_point_two_k_voltage = [3.6, 8.4, 11.4, 13.8, 15.4, 15.8, 16.4, 16.4, 16.6, 16.6, 16.2, 16.2, 16, 15.8, 15.2, 12, 7.28, 4, 2.72, 2.16]
one_point_two_k_frequency = [40.2, 103.5, 160.3, 219, 286, 337.4, 401.9, 463.1, 526.3, 579, 642.6, 704.7, 766.8, 822.3, 1172.3, 2080.7, 4970.2, 10020, 15620, 20700]

three_point_three_k_voltage = [8.8, 16.2, 18.6, 19.4, 20, 20, 20.2, 20.2, 20.2, 20.2, 20, 20, 19.8, 19.8, 19.6, 18.4, 14.8, 10, 7.2, 5.6]
three_point_three_k_frequency = [39.1, 103.3, 160.1, 219.6, 280.2, 341.5, 403.9, 461.2, 521.9, 580.9, 641.8, 692.6, 761, 816.6, 1027.6, 2123, 5111.6, 10080, 15430, 20490]

four_point_five_k_voltage = [11.2, 18.2, 19.8, 20.6, 20.6, 20.8, 20.8, 20.8, 20.8, 20.8, 20.6, 20.6, 20.6, 20.6, 20.2, 19.4, 17, 12.2, 9.6, 7.4]
four_point_five_k_frequency = [38.7, 101.5, 159.9, 223.3, 278.6, 342.4, 398, 455.5, 523.9, 582.3, 643.1, 695.3, 761.2, 821, 1012.3, 2051.1, 5008.1, 10360, 15270, 20570]

# Normalize voltage
def normalize_voltage(voltage):
    return np.array(voltage) / max(voltage)

one_point_two_k_voltage_normalized = normalize_voltage(one_point_two_k_voltage)
three_point_three_k_voltage_normalized = normalize_voltage(three_point_three_k_voltage)
four_point_five_k_voltage_normalized = normalize_voltage(four_point_five_k_voltage)

# Convert frequency to angular frequency (ω = 2πf)
def angular_frequency(frequency):
    return 2 * np.pi * np.array(frequency)

one_point_two_k_omega = angular_frequency(one_point_two_k_frequency)
three_point_three_k_omega = angular_frequency(three_point_three_k_frequency)
four_point_five_k_omega = angular_frequency(four_point_five_k_frequency)

# Plotting
plt.figure(figsize=(10, 6))

# Plot for 1.2 kΩ
plt.plot(one_point_two_k_omega, one_point_two_k_voltage_normalized, label='1.2 kΩ', marker='o')

# Plot for 3.3 kΩ
plt.plot(three_point_three_k_omega, three_point_three_k_voltage_normalized, label='3.3 kΩ', marker='s')

# Plot for 4.5 kΩ
plt.plot(four_point_five_k_omega, four_point_five_k_voltage_normalized, label='4.5 kΩ', marker='^')

# Labels and title
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Normalized Voltage')
plt.title('Normalized Voltage vs Angular Frequency')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
