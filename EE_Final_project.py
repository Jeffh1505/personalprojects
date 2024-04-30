def find_highest_voltages(filename):
    voltages = {}
    with open(filename, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            parts = line.split()
            frequency = float(parts[0])
            # Extracting voltage from the second part of the line
            voltage_str = parts[1]
            # Extracting the numerical part of the voltage string and converting to float
            voltage = float(voltage_str.split('dB')[0])
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
