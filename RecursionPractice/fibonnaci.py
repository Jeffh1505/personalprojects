
def fib(n):
    cache = {}
    if n == 0 or n == 1:
        return 1
    if fib(n) in cache:
        return cache[n]
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(5))