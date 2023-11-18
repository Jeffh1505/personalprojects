def outer(a, b):
    a = a ** 2
    def inner(a, b):
        return a + b
    return inner(a, b) + 5

print(outer(5, 3))