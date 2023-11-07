def sum_num(n):
    if n == 1:
        return n
    else:
        return sum_num(n-1) 
    
print(sum_num(10))