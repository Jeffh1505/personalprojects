import re

def find_highest_voltages(filename):
    voltages = {}
    with open(filename, 'r') as file:
        file.readline()  # Skip the first line
        for line in file:
            match = re.match(r'^\s*(-?\d+\.\d+e[+-]\d+)\s+\((-?\d+\.\d+e[+-]\d+).*\)$', line)
            if match:
                voltage = float(match.group(1))
                frequency = float(match.group(2))
                voltages[voltage] = frequency
    
    highest_voltages = sorted(voltages.keys(), reverse=True)[:2]
    highest_frequencies = [voltages[voltage] for voltage in highest_voltages]
    
    return highest_voltages, highest_frequencies

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    highest_voltages, highest_frequencies = find_highest_voltages(filename)
    print("Highest Output Voltages and Corresponding Frequencies:")
    for voltage, frequency in zip(highest_voltages, highest_frequencies):
        print("Voltage:", voltage, "Frequency:", frequency)
