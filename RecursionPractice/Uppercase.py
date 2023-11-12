def uppercase(str, i=0):
    if str[i].isupper():
        return str[i]
    else:
        return uppercase(str, i+1)
    

print(uppercase("geeksforGeekS"))