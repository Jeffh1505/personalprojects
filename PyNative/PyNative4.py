try:
    user_input = int(input("Please input a number: "))

    for i in range(1, 11):
        print ( i * user_input)
except ValueError:
    print("That is not a number")