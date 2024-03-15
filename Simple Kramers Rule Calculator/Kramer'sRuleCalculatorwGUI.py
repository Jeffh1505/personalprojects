import tkinter as tk
import re
import numpy as np

def fraction_parse_input(input_str: str) -> float:
    # Check if the input is a fraction
    fraction_match = re.match(r'^(\d+)/(\d+)$', input_str)
    if fraction_match:
        numerator = int(fraction_match.group(1))
        denominator = int(fraction_match.group(2))
        return float(numerator / denominator)
    # If not a fraction, assume regular number
    return float(input_str)

def two_by_two(x1: float, x2: float, y1: float, y2: float, c1: float, c2: float) -> str:
    # This function calculates a two by two linear system of equations
    full_matrix = np.array([[x1, y1], [x2, y2]])
    full_matrix_determinant = np.linalg.det(full_matrix)
    x_determinant_matrix = np.array([[c1, y1], [c2, y2]])
    x_determinant = np.linalg.det(x_determinant_matrix)
    x = x_determinant / full_matrix_determinant
    y_determinant_matrix = np.array([[x1, c1], [x2, c2]])
    y_determinant = np.linalg.det(y_determinant_matrix)
    y = y_determinant / full_matrix_determinant
    return f"x = {x}\n y = {y}"

def three_by_three(x1: float, x2: float, x3: float, y1: float, y2: float, y3: float,
                   z1: float, z2: float, z3: float, c1: float, c2: float, c3: float) -> str:
    # This function calculates a three by three system of equations
    full_matrix = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
    full_matrix_determinant = np.linalg.det(full_matrix)
    x_determinant_matrix = np.array([[c1, y1, z1], [c2, y2, z2], [c3, y3, z3]])
    x_determinant = np.linalg.det(x_determinant_matrix)
    x = x_determinant / full_matrix_determinant
    y_determinant_matrix = np.array([[x1, c1, z1], [x2, c2, z2], [x3, c3, z3]])
    y_determinant = np.linalg.det(y_determinant_matrix)
    y = y_determinant / full_matrix_determinant
    z_determinant_matrix = np.array([[x1, y1, c1], [x2, y2, c2], [x3, y3, c3]])
    z_determinant = np.linalg.det(z_determinant_matrix)
    z = z_determinant / full_matrix_determinant
    return f"x = {x}\n y = {y}\n z = {z}"

def CramerGUI():
    window = tk.Tk()
    window.title("Cramer's Rule calculator")
    window.geometry("400x400")

    label = tk.Label(window, text="Would you like to solve a two by two (2) or three by three (3) system of equations?: ")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    x1_label = tk.Label(window, text="Enter x1:")
    x1_label.pack()
    x1_entry = tk.Entry(window)
    x1_entry.pack()

    x2_label = tk.Label(window, text="Enter x2:")
    x2_label.pack()
    x2_entry = tk.Entry(window)
    x2_entry.pack()

    y1_label = tk.Label(window, text="Enter y1:")
    y1_label.pack()
    y1_entry = tk.Entry(window)
    y1_entry.pack()

    y2_label = tk.Label(window, text="Enter y2:")
    y2_label.pack()
    y2_entry = tk.Entry(window)
    y2_entry.pack()

    c1_label = tk.Label(window, text="Enter c1:")
    c1_label.pack()
    c1_entry = tk.Entry(window)
    c1_entry.pack()

    c2_label = tk.Label(window, text="Enter c2:")
    c2_label.pack()
    c2_entry = tk.Entry(window)
    c2_entry.pack()

    x3_label = tk.Label(window, text="Enter x3:")
    x3_label.pack()
    x3_entry = tk.Entry(window)
    x3_entry.pack()

    y3_label = tk.Label(window, text="Enter y3:")
    y3_label.pack()
    y3_entry = tk.Entry(window)
    y3_entry.pack()

    z1_label = tk.Label(window, text="Enter z1:")
    z1_label.pack()
    z1_entry = tk.Entry(window)
    z1_entry.pack()

    z2_label = tk.Label(window, text="Enter z2:")
    z2_label.pack()
    z2_entry = tk.Entry(window)
    z2_entry.pack()

    c3_label = tk.Label(window, text="Enter c3:")
    c3_label.pack()
    c3_entry = tk.Entry(window)
    c3_entry.pack()
    def calculate_result():
        choice = entry.get()
        if choice == "2":
            x1 = fraction_parse_input(x1_entry.get())
            x2 = fraction_parse_input(x2_entry.get())
            y1 = fraction_parse_input(y1_entry.get())
            y2 = fraction_parse_input(y2_entry.get())
            c1 = fraction_parse_input(c1_entry.get())
            c2 = fraction_parse_input(c2_entry.get())
            result_text.set(two_by_two(x1, x2, y1, y2, c1, c2))
        elif choice == "3":
            x1 = fraction_parse_input(x1_entry.get())
            x2 = fraction_parse_input(x2_entry.get())
            x3 = fraction_parse_input(x3_entry.get())
            y1 = fraction_parse_input(y1_entry.get())
            y2 = fraction_parse_input(y2_entry.get())
            y3 = fraction_parse_input(y3_entry.get())
            z1 = fraction_parse_input(z1_entry.get())
            z2 = fraction_parse_input(z2_entry.get())
            z3 = fraction_parse_input(z3_entry.get())
            c1 = fraction_parse_input(c1_entry.get())
            c2 = fraction_parse_input(c2_entry.get())
            c3 = fraction_parse_input(c3_entry.get())
            result_text.set(three_by_three(x1, x2, x3, y1, y2, y3, z1, z2, z3, c1, c2, c3))
    result_label = tk.Label(window, text="Result:")
    result_label.pack()

    result_text = tk.StringVar()
    result_display = tk.Label(window, textvariable=result_text)
    result_display.pack()

    calculate_button = tk.Button(window, text="Calculate", command=calculate_result)
    calculate_button.pack()

    window.mainloop()

if __name__ == "__main__":
    CramerGUI()
