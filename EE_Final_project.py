import re

# Specify the path to your text file
file_path = "C:\Users\summe\OneDrive\Documents\LTspice\Draft9.txt"

# Read data from the text file
try:
    with open(file_path, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please provide the correct file path.")
    exit(1)

# Extract frequencies and voltages
lines = data.strip().split("\n")
freqs = []
voltages = []
for line in lines[1:]:
    freq, voltage = re.findall(r"[-+]?\d*\.\d+|\d+", line)
    freqs.append(float(freq))
    voltage_dB, voltage_phase = re.findall(r"[-+]?\d*\.\d+|\d+", voltage)
    voltages.append(float(voltage_dB))

# Find indices of top two voltages
sorted_indices = sorted(range(len(voltages)), key=lambda i: voltages[i], reverse=True)
top_freq1 = freqs[sorted_indices[0]]
top_freq2 = freqs[sorted_indices[1]]

# Print results
print(f"Frequency with highest voltage: {top_freq1:.2f} Hz")
print(f"Second highest voltage frequency: {top_freq2:.2f} Hz")
