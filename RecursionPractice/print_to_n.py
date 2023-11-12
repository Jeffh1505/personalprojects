def print_to_n(n):
    if n == 1:
        return print(n, end=" ")
    else:
        print(n, end=" ")
        return print_to_n(n-1)
    


print_to_n(5)