def harmonic_sum(n):
    if n == 0:
        return 0
    else:
        return (1/n) + harmonic_sum(n-1)
    

print(harmonic_sum(6))