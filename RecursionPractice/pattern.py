def pattern(n, m, flag):
    if flag == False and m == n:
        return 
    if flag == True:
        if m - 5 > 0:
            pattern(n, m-5, flag=True)
        else:
            flag=False
            pattern(n,m-5, flag)

    else:
        pattern(n, m+5, False)


print(pattern(16, 16, True))