def outer(a, b):
    def inner(a, b):
        return a + b
    return inner(a, b) + 5

print(outer(5, 3))