def sum_digits(n):
    sum_of_digits = 0
    if n == 0:
        return sum_of_digits
    right_most_number = n % 10
    print(right_most_number)
    sum_of_digits += right_most_number 
    
    return sum_digits(n/10)


print(sum_digits(687))