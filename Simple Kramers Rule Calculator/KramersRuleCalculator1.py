import re
import numpy as np

def parse_input(input_str):
    # Check if the input is a fraction
    fraction_match = re.match(r'^(\d+)/(\d+)$', input_str)
    if fraction_match:
        numerator = int(fraction_match.group(1))
        denominator = int(fraction_match.group(2))
        return float(numerator/ denominator)
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

def main():
    while True:
        try:
            user_input = input("Would you like to solve a two by two (2) or three by three (3) system of equations?: ")
            if user_input in ["2", "two", "two by two"]:
                x1 = parse_input(input("What is the first x coefficient?: "))
                x2 = parse_input(input("What is the second x coefficient?: "))
                y1 = parse_input(input("What is the first y coefficient?: "))
                y2 = parse_input(input("What is the second y coefficient?: "))
                c1 = parse_input(input("What is the first constant?: "))
                c2 = parse_input(input("What is the second constant?: "))
                print(two_by_two(x1, x2, y1, y2, c1, c2))
                break
            elif user_input in ["3", "three", "three by three"]:
                x1 = parse_input(input("What is the first x coefficient?: "))
                x2 = parse_input(input("What is the second x coefficient?: "))
                x3 = parse_input(input("What is the third x coefficient?: "))
                y1 = parse_input(input("What is the first y coefficient?: "))
                y2 = parse_input(input("What is the second y coefficient?: "))
                y3 = parse_input(input("What is the third y coefficient?: "))
                z1 = parse_input(input("What is the first z coefficient?: "))
                z2 = parse_input(input("What is the second z coefficient?: "))
                z3 = parse_input(input("What is the third z coefficient?: "))
                c1 = parse_input(input("What is the first constant?: "))
                c2 = parse_input(input("What is the second constant?: "))
                c3 = parse_input(input("What is the third constant?: "))
                print(three_by_three(x1, x2, x3, y1, y2, y3, z1, z2, z3, c1, c2, c3))
                break
            else:
                raise ValueError
        except ValueError:
            print("That is not a valid input, please input a valid system of equations.")

if __name__ == "__main__":
    main()
