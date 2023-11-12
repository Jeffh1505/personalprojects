def geometric_series(n):
    if n == 0:
        return 1
    else:
        return (1/(3**n)) + (1/(3**geometric_series(n-1)))
    

print(geometric_series(5))