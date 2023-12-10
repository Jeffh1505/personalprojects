def pos(n):
    ## Write the code
    for i in range(n, 0, -1):
         print(i-1, end=" ")
    
def neg(n):
    ##Write the code
    for i in range(n,1, 1):
         print(i, end=" ")

n = int(input())

if n == 0:
     print("n is already 0")
elif n > 0:
     pos(n)
elif n < 0:
     neg(n)