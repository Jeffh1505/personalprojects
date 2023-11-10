def sum_digits(n):
    sum_of_digits = 0
    if n == 0:
        return sum_of_digits
    right_most_number = n % 10
    print(right_most_number)
    sum_of_digits = right_most_number + sum_digits(n/10)
    print("Sum:",sum_of_digits)  
    return sum_of_digits


print(sum_digits(687))