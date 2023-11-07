def sum_num(n):
    if n == 1:
        return 1
    else:
        return sum_num(n-1) + sum_num(n-2)
    
print(sum_num(10))