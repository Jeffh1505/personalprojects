def main():
    n = int(input("What is your number? "))
    print(f"Your number's digits sum to: {sum_digits(n)}")

def sum_digits(n):
    sum_of_digits = 0
    if n == 0:
        return sum_of_digits
    right_most_number = n % 10
    sum_of_digits = right_most_number + sum_digits(n//10) 
    return sum_of_digits


if __name__ == "__main__":
    main()