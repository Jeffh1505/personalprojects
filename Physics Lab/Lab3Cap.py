import numpy as np
import matplotlib.pyplot as plt

# Constants
V0 = 5  # Initial voltage in volts
tau = 0.8e-3  # Time constant in seconds (0.8 ms)
t = np.linspace(0, 5*tau, 1000)  # Time from 0 to 5 time constants

# Voltage across the capacitor as a function of time
V = V0 * (1 - np.exp(-t / tau))

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(t * 1000, V, label=f'RC Circuit (τ = {tau*1000:.1f} ms)', color='blue')
plt.title('Voltage across a Capacitor in an RC Circuit')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.show()
