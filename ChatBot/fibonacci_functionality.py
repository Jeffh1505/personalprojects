cache = {}
def fib(n):
    if n == 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]
    result =  fib(n-1) + fib(n-2)
    cache[n] = result             
    return result
def main():
    user_input = int(input("What number of the Fibonnaci sequence would you like? "))    
    print(fib(user_input))

if __name__ == "__main__":
    main()