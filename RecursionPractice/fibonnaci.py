cache = {}
def fib(n):
    if n == 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]
    result =  fib(n-1) + fib(n-2)
    cache[n] = result             
    return result

user_input = int(input("What number of the Fibonnaci sequnce would you like? "))    
print(fib(user_input))