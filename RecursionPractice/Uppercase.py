def uppercase(str, i):
    if str[i].isupper():
        return str[i]
    else:
        return uppercase(str, i+1)
    

print(uppercase("hellO", 0))