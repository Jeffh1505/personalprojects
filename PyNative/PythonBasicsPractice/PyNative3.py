try:
    user_input = int(input("Please input a number: "))
    s = 0
    for i in range(user_input + 1):
        s += i

    print(s)
except ValueError:
    print("That is not a number")