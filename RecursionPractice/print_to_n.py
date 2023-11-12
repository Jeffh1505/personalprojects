def print_to_n(n):
    if n == 1:
        return n
    else:
        return print(print_to_n(n-1))
    


print_to_n(5)