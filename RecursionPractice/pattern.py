def pattern(n, m, flag):
    print(m)
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


pattern(10, 10, True)