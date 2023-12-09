def rotate_right(message, steps):
    result = message
    for i in range(steps):
        result[0] = message[-1] 
        result[1:] = message[0:len(message)-1]
        message = result
    return result

print(rotate_right('python', 3))