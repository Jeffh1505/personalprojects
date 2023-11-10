def increasing(start, out, n):
    if n == 0:
        return print(out, end=" ")
    
    for i in range(start, 10):
         
        # append current digit to number
        str1 = out + str(i)
 
        # recurse for next digit
        increasing(i + 1, str1, n - 1)


increasing(0, "", 3)