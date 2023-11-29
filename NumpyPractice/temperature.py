import numpy as np

temps_in_farenheit = np.array([0., 12., 45.21, 34., 99.91, 32.])

temps_in_celsius = (temps_in_farenheit - 32) * (5/9)

print(temps_in_celsius)