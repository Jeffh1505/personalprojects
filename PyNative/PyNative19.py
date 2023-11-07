def even_numbers(n, x):
    if n == x:
        return n
    else:
        return even_numbers(n + 1, x) % 2
    

print(even_numbers(4, 30))