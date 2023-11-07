def exponent(base, exp):
    if exp == 0:
        return 1
    else:
        result = base * exponent(base, exp - 1)
        return result
    
print(exponent(5,4))