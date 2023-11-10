def main():
    n = int(input("What is your number? "))
    pattern(n, n, True)

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

if __name__ == "__main__":
    main()