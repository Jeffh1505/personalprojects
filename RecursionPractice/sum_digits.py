def sum_digits(n):
    sum_of_digits = 0
    if n == 0:
        return sum_of_digits
    right_most_number = n % 10
    sum_of_digits = right_most_number + sum_digits(n//10) 
    return sum_of_digits


print(sum_digits(125))