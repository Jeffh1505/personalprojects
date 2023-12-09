def rotate_right(message, steps):
    encrypted_string = message
    for i in range(steps):
        encrypted_string[0] = message[-1] 
        encrypted_string[1:] = message[:len(message)-1]
    return encrypted_string

print(rotate_right('python', 3))