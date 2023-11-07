def sum_num(n, x):
    if n == x:
        return n
    else:
        return sum_num(n + 1, x) + n
    
print(sum_num(0, 10))